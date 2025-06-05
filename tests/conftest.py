import os
import time
import pytest
import requests
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.events import EventFiringWebDriver
from Provineer_regression_tests.utilities.logger import Logger
from Provineer_regression_tests.utilities.allure_event_listener import AllureSeleniumEventListener

@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize WebDriver with Allure Event Listener"""
    selenium_url = os.getenv("SELENIUM_REMOTE_URL")
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")

    if selenium_url:
        for _ in range(10):
            try:
                response = requests.get(selenium_url + "/status")
                if response.status_code == 200:
                    break
            except Exception:
                time.sleep(1)
        else:
            raise RuntimeError("Selenium Grid is not responding after 10 attempts")

        driver = webdriver.Remote(
            command_executor=selenium_url,
            options=options
        )
    else:
        from selenium.webdriver.chrome.service import Service as ChromeService
        from webdriver_manager.chrome import ChromeDriverManager

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    # Wrap driver with Event Listener for logging and Allure steps
    event_listener = AllureSeleniumEventListener()
    driver = EventFiringWebDriver(driver, event_listener)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to add logs and screenshot to Allure after each test"""
    outcome = yield
    rep = outcome.get_result()

    # Attach log only after the call phase (test execution)
    if rep.when == "call":
        # Attach log file if exists
        if os.path.exists(Logger.file_name):
            with open(Logger.file_name, "rb") as f:
                allure.attach(f.read(), name="Test Log", attachment_type=allure.attachment_type.TEXT)

        # Attach screenshot if test failed
        if rep.failed:
            driver = item.funcargs.get("driver")
            if driver:
                try:
                    allure.attach(driver.get_screenshot_as_png(), name="Screenshot on Failure", attachment_type=allure.attachment_type.PNG)
                except Exception as e:
                    Logger.error(f"Failed to capture screenshot: {e}")