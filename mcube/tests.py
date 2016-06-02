import os

from .models import PageView
from .database import info
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
local_login_url = "http://127.0.0.1:8000/newuser/"
# These basic tests are to be used as an example for running tests in S2I
# and OpenShift when building an application image.
class PageViewModelTest(TestCase):
    def test_viewpage_model(self):
        pageview = PageView.objects.create(hostname='localhost')
        pagetest = PageView.objects.get(hostname='localhost')
        self.assertEqual(pagetest.hostname, 'localhost')

class PageViewTest(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

class DbEngine(TestCase):
    def setUp(self):
        os.environ['ENGINE'] = 'MySQL'

    def test_engine_setup(self):
        settings = info()
        self.assertEqual(settings['engine'], 'MySQL')
        self.assertEqual(settings['is_mysql'], True)

class CreateUserBehaviorTest(TestCase):
    def create_client(self):
        self.driver = webdriver.Chrome()

    def create_user(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/newuser/")
        assert "MTrivia" in driver.title
        elem = driver.find_element_by_name("username")
        elem.send_keys("triviaman")
        elem.send_keys(Keys.TAB)
        elem.send_keys("triviaman@gmail.com")
        elem.send_keys(Keys.TAB)
        elem.send_keys("Trivia")
        elem.send_keys(Keys.TAB)
        elem.send_keys("Man")
        elem.send_keys(Keys.TAB)
        elem.send_keys("password")
        driver.find_element_by_name("submit").click()

    def test_login(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        assert "MTrivia" in driver.title
        elem = driver.find_element_by_name("username")
        elem.send_keys("triviaman")
        elem.send_keys(Keys.TAB)
        elem.send_keys("password")
        driver.find_element_by_name("login").click()

    def close_client(self):
           self.driver.close()
