from selenium.webdriver.common.by import By

from seleniumPython.data.user_provider import get_user
from seleniumPython.pages.account.account_page import AccountPage
from seleniumPython.pages.base_page import BasePage

class LoginPage(BasePage):
    USER_NAME_INPUT_LOCATOR = (By.XPATH, '//input[@name=\'username\']')
    USER_PASSWORD_INPUT_LOCATOR = (By.XPATH, '//input[@name=\'password\']')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//button[@type=\'submit\']')

    def __init__(self, driver):
        super().__init__(driver)

    def enter_credentials(self, user_name):
        user = get_user(user_name)
        self._wait_element(*self.USER_NAME_INPUT_LOCATOR)
        self.enter_username(user['email'])
        self.enter_password(user['password'])
        return self

    def enter_username(self, email):
        self._find_element(*self.USER_NAME_INPUT_LOCATOR).send_keys(email)

    def enter_password(self, password):
        self._find_element(*self.USER_PASSWORD_INPUT_LOCATOR).send_keys(password)

    def click_login(self):
        self._find_element(*self.LOGIN_BUTTON_LOCATOR).click()
        return AccountPage(self.driver)