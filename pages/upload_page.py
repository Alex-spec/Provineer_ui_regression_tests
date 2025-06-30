from base.base_methods import BasePage
from selenium.webdriver.common.by import By
from utilities.logger import Logger
import allure

class UploadPageLocators:
    UPLOAD_FILE = (By.XPATH, "//input[@type='file']")
    PROCEED_BUTTON = (By.XPATH, "//button[text()='Proceed']")
    NAME_FIELD = (By.XPATH, "//input[@type='text']")
    VERSION_DROPDOWN = (By.XPATH, "(//div[contains(@class, 'MuiOutlinedInput-root')])[3]")
    VERSION_VALUE = (By.XPATH, "//li[@value='1.0']")
    CATEGORY_DROPDOWN = (By.XPATH, "(//div[contains(@class, 'MuiOutlinedInput-root')])[4]")
    CATEGORY_VALUE = (By.XPATH, "//li[@value='robot']")
    DESCRIPTION_FIELD = (By.XPATH, "(//div[contains(@class, 'MuiOutlinedInput-root')])[5]")
    TEXTAREA = (By.XPATH, "//textarea")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Continue']")
    SIGNATURE = (By.XPATH, "//canvas[@width='464']")
    SUMMARY_IMAGE = (By.XPATH, "(//div[@class='MuiBox-root css-xa5bjj'])[1]")
    PROOF_IMAGE = (By.XPATH, "(//div[@class='MuiBox-root css-xa5bjj'])[2]")
    PROVINEER_BUTTON = (By.XPATH, "//button[text()='Provineer']")
    SUCCESSFUL_MESSAGE = (By.XPATH, "//h6[text()='Successful']")

class UploadPageGetters(BasePage):
    def get_browse_button(self):
        return self.wait_for_presence(UploadPageLocators.UPLOAD_FILE)

    def get_proceed_button(self):
        return self.wait_for_clickable(UploadPageLocators.PROCEED_BUTTON)

    def get_name_input(self):
        return self.wait_for_clickable(UploadPageLocators.NAME_FIELD)

    def get_version_dropdown(self):
        return self.wait_for_clickable(UploadPageLocators.VERSION_DROPDOWN)

    def get_version_value(self):
        return self.wait_for_clickable(UploadPageLocators.VERSION_VALUE)

    def get_category_dropdown(self):
        return self.wait_for_clickable(UploadPageLocators.CATEGORY_DROPDOWN)

    def get_category_value(self):
        return self.wait_for_clickable(UploadPageLocators.CATEGORY_VALUE)

    def get_description_field(self):
        return self.wait_for_clickable(UploadPageLocators.DESCRIPTION_FIELD)

    def get_textarea(self):
        return self.wait_for_presence(UploadPageLocators.TEXTAREA)

    def get_continue_button(self):
        return self.wait_for_clickable(UploadPageLocators.CONTINUE_BUTTON)

    def get_signature_field(self):
        return self.wait_for_presence(UploadPageLocators.SIGNATURE)

    @staticmethod
    def get_summary_image():
        return UploadPageLocators.SUMMARY_IMAGE

    @staticmethod
    def get_proof_image():
        return UploadPageLocators.PROOF_IMAGE

    def get_provineer_button(self):
        return self.wait_for_clickable(UploadPageLocators.PROVINEER_BUTTON)

    @staticmethod
    def get_successful_message():
        return UploadPageLocators.SUCCESSFUL_MESSAGE

class UploadPageActions(UploadPageGetters):
    def upload_file(self, file_path):
        self.get_browse_button().send_keys(file_path)
        print("File uploaded")

    def click_proceed_button(self):
        self.get_proceed_button().click()
        print("Proceed button clicked")

    def enter_name_input(self, name):
        self.get_name_input().send_keys(name)
        print("Filled in name input")

    def click_version_dropdown(self):
        self.get_version_dropdown().click()
        self.get_version_value().click()
        print("Clicked version dropdown")

    def click_category_dropdown(self):
        self.get_category_dropdown().click()
        self.get_category_value().click()
        print("Clicked category dropdown")

    def click_description_field(self):
        self.get_description_field().click()
        self.get_textarea().send_keys("Lorem ipsum dolor")
        print("Filled in description form")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Clicked continue button")

    def click_signature_field(self):
        self.get_signature_field().click()
        print("Clicked signature field")

    def click_provineer_button(self):
        self.get_provineer_button().click()
        print("Clicked provineer button")

class UploadPageSteps(UploadPageActions):
    def upload_page(self):
        with allure.step("Testing upload new file"):
            Logger.add_start_step(method="Testing upload new file")
        file_path = "/app/files_to_upload/test_cat.jpg"
        self.upload_file(file_path)
        self.click_proceed_button()
        self.enter_name_input("Test")
        self.click_version_dropdown()
        self.click_category_dropdown()
        self.click_description_field()
        self.click_continue_button()
        self.upload_file(file_path)
        self.click_continue_button()
        self.click_signature_field()
        self.click_continue_button()
        self.assert_word(self.get_summary_image(), "test_cat")
        self.assert_word(self.get_proof_image(), "test_cat")
        # self.click_provineer_button()
        # self.assert_word(self.get_successful_message(), "Successful")
        Logger.add_end_step(url=self.driver.current_url, method="Testing upload new file")

