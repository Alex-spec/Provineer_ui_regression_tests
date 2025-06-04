import time
from Provineer_regression_tests.pages.login_page import LoginPageSteps
from Provineer_regression_tests.pages.dashboard_page import DashboardPageSteps
from Provineer_regression_tests.pages.upload_page import UploadPageSteps


def test_upload_new_file(driver):
    print("Start checking new file upload")
    lp = LoginPageSteps(driver)
    lp.login_page()
    up = UploadPageSteps(driver)
    up.upload_page()

def test_shared_feature(driver):
    lp = LoginPageSteps(driver)
    lp.login_page()
    dp = DashboardPageSteps(driver)
    dp.test_uploads_dashboard()

def test_proofs_and_certificates(driver):
    lp = LoginPageSteps(driver)
    lp.login_page()
    dp = DashboardPageSteps(driver)
    dp.check_e_certificate_feature()


