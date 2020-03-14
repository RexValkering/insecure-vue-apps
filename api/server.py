from flask import Flask, request, abort
from flask_restful import Resource, Api
from flask_cors import CORS
from json import dumps, loads
import sqlite3
import uuid
import random
import string
import hashlib
import os
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


app = Flask(__name__)
api = Api(app)

if not os.path.exists("config.yaml"):
    exit("Please create a config.yaml first.")
CONFIG = load(open('config.yaml').read(), Loader=Loader)

# Avoid CORS errors.
CORS(app, resources={r"/*": {"origins": "*"}})


if not os.path.exists("./instances"):
    os.mkdir("instances")


def generate_id():
    return str(uuid.uuid4())


def generate_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class RestDatabase(object):
    """Simple controller for the database."""

    def __init__(self, database):
        self.database = database
        self._init_db()
        self._init_data()

    def _init_db(self):
        self.query("""CREATE TABLE IF NOT EXISTS projects  (
            id text primary key,
            project_name text,
            flag text
        )""")

        self.query("""CREATE TABLE IF NOT EXISTS instances  (
            id text primary key,
            project_id text
        )""")

        self.query("""CREATE TABLE IF NOT EXISTS credentials  (
            id text primary key,
            instance_id text,
            username text,
            password text,
            admin int
        )""")

        self.query("""CREATE TABLE IF NOT EXISTS tokens  (
            id text primary key,
            instance_id text,
            user_id text
        )""")

        self.query("""CREATE TABLE IF NOT EXISTS data  (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            instance_id text,
            entry text
        )""")

    def _init_data(self):
        flags = CONFIG["beautiful_quotes_flag"], CONFIG["beautiful_quotes_2_flag"], CONFIG["beautiful_quotes_3_flag"]

        if not self.get_rows("SELECT * FROM projects"):
            self.query("""INSERT INTO projects (id, project_name, flag) VALUES
                (?, 'beautiful-quotes', ?),
                (?, 'beautiful-quotes-2', ?),
                (?, 'beautiful-quotes-3', ?)""", (generate_id(), flags[0], generate_id(), flags[1], generate_id(), flags[2]))

    def query(self, query, variables=tuple()):
        """Execute a query in the database."""
        conn = sqlite3.connect(self.database)
        c = conn.cursor()
        if variables:
            c.execute(query, variables)
        else:
            c.execute(query)
        conn.commit()
        c.close()
        conn.close()

    def get_rows(self, query, variables=tuple(), single=False):
        """Get one or multiple rows."""
        data = None
        conn = sqlite3.connect(self.database)
        c = conn.cursor()

        if variables:
            c.execute(query, variables)
        else:
            c.execute(query)

        if single:
            data = c.fetchone()
        else:
            data = c.fetchall()

        c.close()
        conn.close()
        return data

    def get_row(self, query, variables=tuple()):
        """Fetch a single row."""
        return self.get_rows(query, variables, single=True)

    def get_instance(self):
        authorization = request.headers.get('Authorization')
        if not authorization or len(authorization) < 8:
            abort(401)

        token = authorization[7:]
        user = self.validate_token(token)

        if not user:
            abort(401)

        return user[1]

    def get_user(self):
        authorization = request.headers.get('Authorization')
        if not authorization or len(authorization) < 8:
            abort(401)

        token = authorization[7:]
        user = self.validate_token(token)

        if not user:
            abort(401)

        return self.get_row("SELECT * FROM credentials WHERE id = ?", (user[2], ))

    def validate_token(self, token):
        return self.get_row("SELECT * FROM tokens WHERE id = ?", (token, ))


DATABASE = RestDatabase('database.db')


class Polling(Resource):
    def get(self, last_id):
        return {'entries': DATABASE.get_rows("""
            SELECT credentials.username, MAX(data.id), projects.project_name FROM data
            JOIN credentials ON data.instance_id=credentials.instance_id
            JOIN instances ON instances.id = credentials.instance_id
            JOIN projects ON projects.id = instances.project_id
            WHERE data.id > ? AND credentials.admin=1
            GROUP BY credentials.username""", (last_id,))}


class Projects(Resource):
    def get(self):
        return {'projects': DATABASE.get_rows('SELECT id, project_name FROM projects')}


class Instances(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        project_name = json_data["project_id"]

        if not project_name:
            abort(400)

        # Check if project exists
        project = DATABASE.get_row(
            'SELECT id FROM projects WHERE project_name = ?', (project_name,))
        if not project:
            abort(400)

        project_id = project[0]
        instance_id = generate_id()
        user_name = generate_string()
        user_password = generate_string()
        user_hash = hashlib.sha256(user_password.encode('utf-8')).hexdigest()
        admin_name = generate_string()
        admin_password = CONFIG['master_password']
        admin_hash = hashlib.sha256(admin_password.encode('utf-8')).hexdigest()

        DATABASE.query(
            'INSERT INTO instances (id, project_id) VALUES (?, ?)', (instance_id, project_id))
        DATABASE.query("""INSERT INTO credentials(id, instance_id, username, password, admin) VALUES
                          (?, ?, ?, ?, ?), (?, ?, ?, ?, ?)""",
                       (generate_id(), instance_id, user_name, user_hash, 0,
                        generate_id(), instance_id, admin_name, admin_hash, 1)
                       )

        with open('instances/{}'.format(instance_id), "w") as outfile:
            outfile.write("{}\n".format(project_id))
            outfile.write("user {} {}\n".format(user_name, user_password))
            outfile.write("admin {} {}\n".format(admin_name, admin_password))

        return {'username': user_name, 'password': user_password}


class Data(Resource):

    def get(self):
        instance_id = DATABASE.get_instance()
        rows = DATABASE.get_rows(
            'SELECT * FROM data WHERE instance_id IS NULL OR instance_id = ?', (instance_id, ))
        return [loads(row[2]) for row in rows]

    def post(self):
        instance_id = DATABASE.get_instance()
        username = DATABASE.get_user()[2]
        data = request.get_json(force=True)
        data['submitter'] = username
        entry = dumps(data)

        DATABASE.query(
            "INSERT INTO data (instance_id, entry) VALUES (?, ?)", (instance_id, entry))

        return data

    def delete(self):
        instance_id = DATABASE.get_instance()
        DATABASE.query("DELETE FROM data WHERE instance_id = ?",
                       (instance_id, ))


class Login(Resource):

    def get(self):
        user = DATABASE.get_user()
        return {
            'username': user[2],
            'admin': user[4]
        }

    def post(self):
        data = request.get_json(force=True)
        username, password = data.get('username'), data.get('password')
        encrypted_password = hashlib.sha256(
            password.encode('utf-8')).hexdigest()

        row = DATABASE.get_row(
            "SELECT * FROM credentials WHERE username = ? AND password = ?", (username, encrypted_password))
        if not row:
            abort(401)

        user_id, instance_id, _, _, is_admin = row

        # Create a new token
        token = generate_string(16)
        DATABASE.query(
            "INSERT INTO tokens (id, instance_id, user_id) VALUES (?, ?, ?)", (
                token, instance_id, user_id)
        )

        greeting = "Welcome, user!"
        if is_admin:
            flag = DATABASE.get_row(
                """SELECT flag FROM projects
                   JOIN instances ON instances.project_id = projects.id
                   WHERE instances.id = ?""", (instance_id, ))
            greeting = "Welcome, admin! Your secret flag is: {}".format(
                flag[0])

        return {
            'token': token,
            'admin': is_admin,
            'instance_id': instance_id,
            'greeting': greeting
        }


class AdminMaker(Resource):

    def post(self):
        user = DATABASE.get_user()
        instance_id = DATABASE.get_instance()

        if not int(user[4]):
            abort(403)

        data = request.get_json(force=True)
        username = data.get('username')

        row = DATABASE.get_row(
            "SELECT * FROM credentials WHERE username = ? AND instance_id = ?", (username, instance_id))
        if not row:
            abort(400)

        DATABASE.query(
            "UPDATE credentials SET admin = 1 WHERE username = ?", (username, ))


class Flag(Resource):

    def get(self):
        user = DATABASE.get_user()
        if not int(user[4]):
            abort(403)

        row = DATABASE.get_row(
            """SELECT p.flag FROM projects p
            JOIN instances i ON i.project_id = p.id WHERE i.id = ?""", (user[1], )
        )

        if not row:
            abort(400)

        return {'flag': row[0]}


api.add_resource(Projects, '/projects')
api.add_resource(Instances, '/instances')
api.add_resource(Data, '/data')
api.add_resource(Login, '/login')
api.add_resource(Polling, '/poll/<last_id>')
api.add_resource(AdminMaker, '/makeadmin')
api.add_resource(Flag, '/flag')


if __name__ == '__main__':
    app.run(port=CONFIG['api_port'], debug=True)
