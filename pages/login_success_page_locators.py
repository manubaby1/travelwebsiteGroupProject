from selenium.webdriver.common.by import By


class LoginSuccessPageLocators:
    LOGIN_STATUS_MESSAGE = (By.XPATH, "//h3[normalize-space()='Login Successfully']")
    SIGN_OFF = (By.XPATH, "//a[normalize-space()='SIGN-OFF']")
    SIGN_ON = (By.XPATH, "//a[normalize-space()='SIGN-ON']")