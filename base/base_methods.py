from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utilities.logger import Logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_clickable(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_visible(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_presence(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, timeout=30):
        self.wait_for_clickable(locator, timeout).click()

    def input_text(self, locator, text, timeout=30):
        self.wait_for_clickable(locator, timeout).send_keys(text)

    def open_site(self, url):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
        except Exception as e:
            print(f"Error while opening the website: {e}")
            raise



