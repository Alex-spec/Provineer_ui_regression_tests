import allure
from selenium.webdriver.support.events import AbstractEventListener
from selenium.common.exceptions import StaleElementReferenceException
from utilities.logger import Logger

class AllureSeleniumEventListener(AbstractEventListener):
    def before_click(self, element, driver):
        """Log and create Allure step before clicking an element"""
        try:
            self._element_tag = element.tag_name
            self._element_text = element.text.strip() if element.text else "No text"
        except StaleElementReferenceException:
            self._element_tag = "stale element"
            self._element_text = "No text"

        message = f"Trying to click on <{self._element_tag}> with text '{self._element_text}'"
        Logger.info(message)
        with allure.step(message):
            pass

    def after_click(self, element, driver):
        """Log after clicking an element"""
        Logger.info(f"Clicked on <{self._element_tag}>")

    def before_navigate_to(self, url, driver):
        """Log and create Allure step before navigating to a URL"""
        message = f"Navigating to URL: {url}"
        Logger.info(message)
        with allure.step(message):
            pass

    def before_change_value_of(self, element, driver):
        """Log and create Allure step before changing value of an element"""
        try:
            tag_name = element.tag_name
        except StaleElementReferenceException:
            tag_name = "stale element"

        message = f"Trying to input into <{tag_name}>"
        Logger.info(message)
        with allure.step(message):
            pass

    def on_exception(self, exception, driver):
        """Log an error and attach a screenshot to Allure in case of an exception"""
        Logger.error(f"Exception occurred: {exception}")
        with allure.step(f"Exception: {exception}"):
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Screenshot on Failure",
                attachment_type=allure.attachment_type.PNG
            )
