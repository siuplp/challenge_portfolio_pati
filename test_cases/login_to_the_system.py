import os
import unittest
from selenium import webdriver

from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.tytle_of_page()
        user_login.tytle_of_page()
        user_login.type_in_email('user10@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()