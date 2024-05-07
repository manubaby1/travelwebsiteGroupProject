from pages.base_page import BasePage
from pages.login_success_page_locators import LoginSuccessPageLocators
from resources.constans import MAX_WAIT_INTERVAL


class LoginSuccessPage(BasePage):

    def get_login_status_message(self):
        return self.find_element(LoginSuccessPageLocators.LOGIN_STATUS_MESSAGE).text

    def sign_off(self):
        return self.find_element(LoginSuccessPageLocators.SIGN_OFF).click()

    def check_sign_in_status(self):
        return self.find_element(LoginSuccessPageLocators.SIGN_ON).text

    def refresh_successpage(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,LoginSuccessPageLocators.SIGN_OFF)
        self.refresh_browser()
