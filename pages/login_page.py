from base.base_methods import BasePage
from selenium.webdriver.common.by import By
from utilities.logger import Logger
import allure

class LoginPageLocators:
    EMAIL = (By.XPATH, "(//input[@type='email'])[1]")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SIGN_IN_BUTTON = (By.XPATH, "(//button[@type='submit'])[1]")

class LoginPageGetters(BasePage):
    def get_email(self):
        return self.wait_for_clickable(LoginPageLocators.EMAIL)

    def get_password(self):
        return self.wait_for_clickable(LoginPageLocators.PASSWORD)

    def get_sign_in_button(self):
        return self.wait_for_clickable(LoginPageLocators.SIGN_IN_BUTTON)

class LoginPageActions(LoginPageGetters):
    def input_email(self, email):
        self.input_text(self.get_email(), email)
        print("Filled in user email")

    def input_password(self, pwd):
        self.input_text(self.get_password(), pwd)
        print("Filled in user password")

    def click_sign_in_button(self):
        self.click_element(self.get_sign_in_button())
        print("Clicked sign in button")

class LoginPageSteps(LoginPageActions):
    def login_page(self):
        with allure.step("User login"):
            Logger.add_start_step(method="User login")
        self.open_site("https://provineer.com/login")
        self.input_email("mebigaw742@pricegh.com")
        self.input_password("qweQwe123#")
        self.click_sign_in_button()
        print(f"Current URL after login: {self.driver.current_url}")
        self.assert_url_contains("provineer.com")
        Logger.add_end_step(url=self.driver.current_url, method="User login")

    def login_account_for_share(self):
        with allure.step("User to test share feature, login"):
            Logger.add_start_step(method="User to test share feature, login")
        self.input_email("alexqamiroshkin@gmail.com")
        self.input_password("qweQwe123#")
        self.click_sign_in_button()
        print(f"Current URL after login: {self.driver.current_url}")
        self.assert_url_contains("provineer.com")
        Logger.add_end_step(url=self.driver.current_url, method="User to test share feature, login")




