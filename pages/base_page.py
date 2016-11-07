from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    url = 'http://one2go.asia/'

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)

    def enter_text_into_field(self, xpath, text):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print('Element is not exist on page, xpath ' + xpath)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            print('Element is not exist on page, xpath ' + xpath)
        field = self.driver.find_element_by_xpath(xpath)
        field.send_keys(text)

    def select_value_in_drop_list(self, xpath, value):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print('Element is not exist on page, xpath ' + xpath)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print('Element is not visible on page, xpath ' + xpath)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            print('Element isn`t clickable, xpath ' + xpath)
        elem = Select(self.driver.find_element_by_xpath(xpath))
        elem.select_by_value(value)

    def click_on_the_object(self, xpath):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print('Element is not exist on page, xpath ' + xpath)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print('Element is not visible on page, xpath ' + xpath)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            print('Element isn`t clickable, xpath ' + xpath)
        elem = self.driver.find_element_by_xpath(xpath)
        elem.click()

    def wait_object(self, xpath):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print('Element is not exist on page, xpath ' + xpath)
