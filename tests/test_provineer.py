import allure
from pages.login_page import LoginPageSteps
from pages.dashboard_page import DashboardPageSteps
from pages.upload_page import UploadPageSteps

@allure.description("Test upload new file")
def test_upload_new_file(driver):
    print("Start checking new file upload")
    lp = LoginPageSteps(driver)
    lp.login_page()
    up = UploadPageSteps(driver)
    up.upload_page()
    print("End checking new file upload")

@allure.description("Test shared feature")
def test_shared_feature(driver):
    print("Start checking shared feature")
    lp = LoginPageSteps(driver)
    lp.login_page()
    dp = DashboardPageSteps(driver)
    dp.test_uploads_dashboard()
    print("End checking shared feature")

@allure.description("Test proofs and certificates")
def test_proofs_and_certificates(driver):
    print("Start checking proofs and certificates")
    lp = LoginPageSteps(driver)
    lp.login_page()
    dp = DashboardPageSteps(driver)
    dp.check_e_certificate_feature()
    print("End checking proofs and certificates")


