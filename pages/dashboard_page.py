import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Provineer_regression_tests.base.base_methods import BasePage
from Provineer_regression_tests.pages.login_page import LoginPageSteps
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Provineer_regression_tests.utilities.logger import Logger
import allure

class DashboardPageLocators:
    AVATAR = (By.XPATH, "//img[@alt='User Avatar']")
    UPLOADS = (By.XPATH, "//span[text()='My uploads']")
    TEST_FILE = (By.XPATH, "//img[@alt='Uploaded produce']")
    SHARE_BUTTON = (By.XPATH, "//*[text()='Share']")
    SHARE_DROPDOWN = (By.XPATH, "(//div[@role='combobox'])[2]")
    ANYONE_OPTIONS = (By.XPATH, "//li[text()='Anyone with the link']")
    PRIVATE_OPTIONS = (By.XPATH, "//li[text()='Private (Only me)']")
    ONLY_INVITED_OPTIONS = (By.XPATH, "//li[text()='Only people invited']")
    PROCEED_BUTTON = (By.XPATH, "//button[text()='Proceed']")
    EMAIL_INPUT = (By.XPATH, "(//input[@type='email'])[2]")
    INVITE_BUTTON = (By.XPATH, "//button[text()='Invite']")
    CLOSE_BUTTON = (By.XPATH, "(//button[@type='button'])[21]")
    LOG_OUT = (By.XPATH, "//span[text()='Log Out']")
    LOGIN_BUTTON = (By.XPATH, "(//button[text()='Login'])[1]")
    SHARED_WITH_ME_BUTTON = (By.XPATH, "//span[text()='Shared with me']")
    SHARED_ASSERT_MESSAGE = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-x1va7p']")

    # Check e-certificate feature locators

    E_CERTIFICATE_BUTTON = (By.XPATH, "//button[text()='View E-Certificate']")
    CERTIFICATE = (By.XPATH, "//canvas[@class='react-pdf__Page__canvas']")

class DashboardPageGetters(BasePage):
    def get_user_avatar(self):
        return self.wait_for_clickable(DashboardPageLocators.AVATAR)

    def get_user_uploads(self):
        return self.wait_for_clickable(DashboardPageLocators.UPLOADS)

    def get_test_file(self):
        return self.wait_for_clickable(DashboardPageLocators.TEST_FILE)

    def get_share_button(self):
        return self.wait_for_clickable(DashboardPageLocators.SHARE_BUTTON)

    def get_share_dropdown(self):
        return self.wait_for_clickable(DashboardPageLocators.SHARE_DROPDOWN)

    def get_private_options(self):
        return self.wait_for_clickable(DashboardPageLocators.PRIVATE_OPTIONS)

    def get_anyone_options(self):
        return self.wait_for_clickable(DashboardPageLocators.ANYONE_OPTIONS)

    def get_proceed_button(self):
        return self.wait_for_clickable(DashboardPageLocators.PROCEED_BUTTON)

    def get_only_invited_options(self):
        return self.wait_for_clickable(DashboardPageLocators.ONLY_INVITED_OPTIONS)

    def get_email_input(self):
        return self.wait_for_clickable(DashboardPageLocators.EMAIL_INPUT)

    def get_invite_button(self):
        return self.wait_for_clickable(DashboardPageLocators.INVITE_BUTTON)

    def get_logout_button(self):
        return self.wait_for_clickable(DashboardPageLocators.LOG_OUT)

    def get_login_button(self):
        return self.wait_for_clickable(DashboardPageLocators.LOGIN_BUTTON)

    def get_shared_with_me(self):
        return self.wait_for_clickable(DashboardPageLocators.SHARED_WITH_ME_BUTTON)

    @staticmethod
    def get_shared_assert_message():
        return DashboardPageLocators.SHARED_ASSERT_MESSAGE

    # Check e-certificate feature getters

    def get_e_certificate_button(self):
        return self.wait_for_clickable(DashboardPageLocators.E_CERTIFICATE_BUTTON)

    def get_certificate(self):
        return self.wait_for_visible(DashboardPageLocators.CERTIFICATE)

class DashboardPageActions(DashboardPageGetters):
    def click_user_avatar(self):
        self.get_user_avatar().click()
        print("Clicked user avatar")

    def click_user_uploads(self):
        self.get_user_uploads().click()
        print("User uploads")


    def click_test_file(self):
        self.get_test_file().click()
        print("Clicked test file")
        self.get_share_button().click()
        print("clicked share button")

    def set_share_options(self):
        self.get_share_dropdown().click()
        self.get_anyone_options().click()
        self.get_share_dropdown().click()
        self.get_private_options().click()
        self.get_proceed_button().click()
        self.get_share_dropdown().click()
        self.get_only_invited_options().click()
        print("Cleared shared files")

    def fill_in_email_input(self, email):
        self.get_email_input().send_keys(email)
        print("Filled in email form to share file")

    def click_invite_button(self):
        self.get_invite_button().click()
        print("Invite button clicked")

    def press_escape_key(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ESCAPE).perform()
        print("Share form closed")

    def click_log_out_button(self):
        self.get_logout_button().click()
        print("Clicked log out button")

    def click_login_button(self):
        self.get_login_button().click()
        print("Clicked login button")

    def click_shared_with_me_button(self):
        self.get_shared_with_me().click()
        print("Clicked shared with me button")

    # Check e-certificate feature actions

    def click_e_certificate_button(self):
        self.get_e_certificate_button().click()
        print("Clicked e-certificate button")

class DashboardPageSteps(DashboardPageActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPageSteps(driver)

    def test_uploads_dashboard(self):
        with allure.step("Testing share feature"):
            Logger.add_start_step(method="Testing share feature")
        self.click_user_avatar()
        self.click_user_uploads()
        self.click_test_file()
        self.set_share_options()
        self.fill_in_email_input("alexqamiroshkin@gmail.com")
        self.click_invite_button()
        self.press_escape_key()
        self.click_user_avatar()
        self.click_log_out_button()
        self.click_login_button()
        self.login_page.login_account_for_share()
        self.click_user_avatar()
        self.click_user_uploads()
        self.click_shared_with_me_button()
        self.assert_word(self.get_shared_assert_message(), "Test Automation")
        Logger.add_end_step(url=self.driver.current_url, method="Testing share feature")

    def check_e_certificate_feature(self):
        with allure.step("Testing e-certificate"):
            Logger.add_start_step(method="Testing e-certificate")
        self.click_user_avatar()
        self.click_user_uploads()
        self.get_test_file().click()
        self.click_e_certificate_button()
        self.get_certificate()
        self.scroll_down(pixels=300)
        self.take_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method="Testing e-certificate")


