from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constans import MAX_WAIT_INTERVAL


class IndexPage(BasePage):

    def click_on_register_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.REGISTER_LINK).click()

    def login(self,user_name,password):
        self.find_element(IndexPageLocators.USER_NAME_TXTBX).send_keys(user_name)
        self.find_element(IndexPageLocators.PASSWORD_TXTBX).send_keys(password)

    def click_on_login_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.LOGIN_SUBMIT_BTN).click()

