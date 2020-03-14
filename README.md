# Change My Vue

## Hacking insecure Vue apps

This project was created for a Cross-Site Scripting (XSS) workshop held in March 2020.
It shows in which ways XSS vulnerabilities can be present in Vue.js code and allows users to learn about these by hacking three different websites.
The exercises of this workshop were inspired by the Vue.js [Security](https://vuejs.org/v2/guide/security.html) page.

## Project demo

The main website and exercises should still be up on:

- https://workshop.rexvalkering.nl/

However, since the worker is not running, your hacks will not work. If you want to try the hacks, you should set this up yourself!

## Project contents

- An exercise website, written in Vue.js, with examples, instructions and exercise pages.
  For each exercise, there are three difficulty levels. This allows people with varying levels of experience to join in.
- Three exercises (Vue.js websites) with different vulnerabilities.
- A backend written in Python which serves as a database API.
- A selenium bot written in Python which acts as an admin user that can be hacked.

The database is segmented into 'instances' so multiple users can try their hand at the exercise without interfering with each other.

## Requirements for the workshop

- A server where you can host four websites and an API on different endpoints, with at least Python and NPM installed.
- An available computer with Python, Chrome & ChromeDriver which can host the selenium bot.

## Preparing the workshop

### Running the exercises locally

1. In the `api` folder, open the `config-sample.yaml` and fill with your config values. Locally, you could use http://localhost:5002 for the API, and http://localhost:8000 for the three exercise websites. You can set your own flags. Save the file as `config.yaml`.
2. Run the server.py. It should create a `database.db` file.
3. Make a copy of the `assets/.env-sample` file, fill in the config values, save as `.env` and copy to the four Vue.js website folders.
4. Choose one of the projects and run it with Vue.
5. Go to the `api` folder and run the worker. Now you're ready to try the exercises yourself.

### Running the exercises in production

If you need help with this, feel free to contact me at *firstnamelastname at gmail dot com*.


