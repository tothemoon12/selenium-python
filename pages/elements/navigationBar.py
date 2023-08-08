from selenium.webdriver.common.by import By

from seleniumPython.pages.base_page import BasePage
from seleniumPython.pages.loginPage.loginPage import LoginPage


class NavigationBar(BasePage):
    NAVIGATION_CONTAINER_BY = (By.XPATH, '//*[@id=\'header-container\']/div')
    LOGIN_BUTTON_PATH = (By.ID, 'topLoginLink')
    POST_NEW_ADD_LINK_LOCATOR = (By.ID, 'postNewAdLink')
    CONVERSATIONS_LOCATOR = (By.ID, 'nav-conversations')

    def wait_for_nav_bar_present(self):
        self.wait_element(*self.NAVIGATION_CONTAINER_BY)

    def click_on_login_button(self):
        self.wait_for_nav_bar_present()
        self.find_element(*self.LOGIN_BUTTON_PATH).click()

    def click_on_conversations_link(self):
        self.wait_for_nav_bar_present()
        self.find_element(*self.CONVERSATIONS_LOCATOR).click()
