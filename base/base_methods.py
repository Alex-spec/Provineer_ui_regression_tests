from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_clickable(self, locator, timeout=30):
        """Wait until the element is clickable."""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_visible(self, locator, timeout=30):
        """Wait until the element is visible."""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_presence(self, locator, timeout=30):
        """Wait until the element is present in the DOM."""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, timeout=30):
        """Finds an element and clicks it."""
        element = self.wait_for_clickable(locator, timeout)
        element.click()

    def input_text(self, locator, text, timeout=30):
        """Finds an element, clears it, and sends keys."""
        element = self.wait_for_clickable(locator, timeout)
        element.clear()
        element.send_keys(text)

    def open_site(self, url):
        """Opens a website and maximizes the window."""
        try:
            self.driver.get(url)
            self.driver.maximize_window()
        except Exception as e:
            print(f"Error while opening the website: {e}")
            raise

    def scroll_down(self, pixels=1000):
        """Scrolls the page down by a specified number of pixels"""
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        print(f"Page scrolled down by {pixels} pixels")

    def take_screenshot(self, file_name='screenshot.png'):
        """Takes a screenshot and saves it to a specified directory."""
        screenshots_dir = 'screen'
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        file_path = os.path.join(screenshots_dir, file_name)
        self.driver.save_screenshot(file_path)
        print(f"Screenshot saved to {file_path}")

    def assert_url_contains(self, partial_url, timeout=15):
        """Asserts that the current URL contains a partial string."""
        WebDriverWait(self.driver, timeout).until(EC.url_contains(partial_url))
        current_url = self.driver.current_url
        assert partial_url in current_url, f"expected '{partial_url}' in '{current_url}'"

    def assert_word(self, locator, expected_text, timeout=30):
        """Check that the element's text matches the expected text."""
        element = self.wait_for_visible(locator, timeout)
        actual_text = element.text.strip()
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"




