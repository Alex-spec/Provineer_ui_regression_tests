import time
import os
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    selenium_url = os.getenv("SELENIUM_REMOTE_URL")
    options = Options()

    if selenium_url:
        for i in range(10):
            try:
                response = requests.get(selenium_url + "/status")
                if response.status_code == 200:
                    break
            except Exception:
                time.sleep(1)
        else:
            raise RuntimeError("Selenium не отвечает после 10 попыток")

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

    yield driver
    driver.quit()

