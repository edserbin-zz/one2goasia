import unittest
from selenium import webdriver

from read_data import return_command_executer


class BaseTest(unittest.TestCase):

    command_executer = return_command_executer()

    def setUp(self):
        desired_cap = {'browser': 'chrome', 'build': 'First build', 'browserstack.debug': 'true'}

        self.driver = webdriver.Remote(
            command_executor=self.command_executer,
            desired_capabilities=desired_cap)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

