from selenium.webdriver.common.by import By
TEST_SITE_URL = "https://demo.guru99.com/test/newtours/index.php"
MAX_WAIT_INTERVAL = 60



class RegisterSuccessPageLocators:
    RESIGSTER_SUCCESS_LBL = (By.XPATH,"//table[@width='492']/*/tr[3]/*/p[3]/*/b")