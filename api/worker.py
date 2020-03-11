from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import requests

import os
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Worker():

    def __init__(self):
        self.processed_quotes = set()
        self.config = load(open('config.yaml').read(), Loader=Loader)
        self.last_message_id = 0

        entries = self.poll_new_data()
        if entries:
            self.last_message_id = max([int(entry[1]) for entry in entries])

        self.handlers = {
            'beautiful-quotes': self.beautiful_quotes_handler,
            'beautiful-quotes-2': self.beautiful_quotes_2_handler,
            'beautiful-quotes-3': self.beautiful_quotes_3_handler,
            'beautiful-regex': self.beautiful_regex_handler
        }

    def poll_new_data(self):
        """Ask the API if we should login as admin."""
        response = requests.get(
            '{}/poll/{}'.format(self.config['api_url'], self.last_message_id))
        data = response.json()['entries']
        return data

    def parse_entry(self, entry):
        """Parse a single polling entry."""
        admin_username = entry[0]
        self.last_message_id = max(self.last_message_id, int(entry[1]))
        project_name = entry[2]

        if project_name in self.handlers:
            self.handlers[project_name](admin_username)
        else:
            print("No such project handler: {}".format(project_name))

    def step(self):
        entries = self.poll_new_data()
        if entries:
            for entry in entries:
                self.parse_entry(entry)

    def run(self):
        while True:
            self.step()
            time.sleep(1)

    def beautiful_quotes_login(self, driver, url, admin_username):
        driver.get(url)
        username = driver.find_element_by_id("username")
        username.clear()
        username.send_keys(admin_username)
        password = driver.find_element_by_id("password")
        password.clear()
        password.send_keys(self.config['master_password'])
        signin = driver.find_element_by_id("button-sign-in")
        signin.click()
        time.sleep(1)

    def beautiful_quotes_handler(self, admin_username):
        driver = webdriver.Chrome()
        try:
            self.beautiful_quotes_login(
                driver, self.config['beautiful_quotes_url'], admin_username)
        except UnexpectedAlertPresentException as error:
            pass
        except Exception as e:
            print(e)
        driver.quit()

    def beautiful_quotes_2_handler(self, admin_username):
        driver = webdriver.Chrome()
        try:
            self.beautiful_quotes_login(
                driver, self.config['beautiful_quotes_2_url'], admin_username)
            link = driver.find_element_by_class_name("link")
            link.click()
            time.sleep(1)
        except UnexpectedAlertPresentException as error:
            pass
        except Exception as e:
            print(e)
        driver.quit()

    def beautiful_quotes_3_handler(self, admin_username):
        driver = webdriver.Chrome()
        try:
            self.beautiful_quotes_login(
                driver, self.config['beautiful_quotes_3_url'], admin_username)


            link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "logout")))
            location = link.location

            action = webdriver.common.action_chains.ActionChains(driver)
            action.move_to_element_with_offset(link, 5, 5)
            action.click()
            action.perform()
            time.sleep(1)
        except UnexpectedAlertPresentException as error:
            pass
        except Exception as e:
            print(e)
        driver.quit()

    def beautiful_regex_handler(self, admin_username):
        pass


worker = Worker()
worker.run()
