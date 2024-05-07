from pages.index_page import IndexPage
from pages.register_page import RegisterPage
from pages.register_success_page import RegisterSuccessPage
from pages.login_success_page import LoginSuccessPage
from resources.constans import TEST_SITE_URL


class TestLogin:

    # Test Case 1 - Registering the user
    def test_register_new_user(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.click_on_register_btn()

        register_page = RegisterPage(driver)
        register_page.register_new_user(username_password[0],username_password[1])

        register_success_page = RegisterSuccessPage(driver)
        register_success_lbl = register_success_page.get_register_success_label()
        assert "Note: Your user name is " + username_password[0] + "." == register_success_lbl, "Test Case 1 Failed due to username assertion error"

    # Test Case 2
    def test_login(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)

        index_page.login(username_password[0],username_password[1])
        index_page.click_on_login_btn()

        login_success_page = LoginSuccessPage(driver)
        login_status_message = login_success_page.get_login_status_message()
        assert "Login Successfully" == login_status_message, "Test failed due to login status mismatch"

    # Test Case 3
    def test_signoff(self, driver):
        login_success_page = LoginSuccessPage(driver)
        login_success_page.sign_off()
        try:
            signoff_status = login_success_page.check_sign_in_status()
        except:
            login_success_page.refresh_successpage()
            signoff_status = login_success_page.check_sign_in_status()
        assert "SIGN-ON" == signoff_status, "test failed"