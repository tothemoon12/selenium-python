from selenium.webdriver.common.by import By

from seleniumPython.pages.base_page import BasePage


class AccountPage(BasePage):
    PAGE_TITLE_LOCATOR = (By.XPATH, '//h3[text()=\'Ваші оголошення\']')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_header_title(self):
        self._wait_element(*self.PAGE_TITLE_LOCATOR)

        return self._find_element(*self.PAGE_TITLE_LOCATOR).text
