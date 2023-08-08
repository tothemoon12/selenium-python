from .base_test import BaseTest
from seleniumPython.pages.homePage.homePage import HomePage


class LoginTest(BaseTest):

    def testLogin(self):
        home_page = HomePage(self.driver)
        (home_page
         .open_login_page()
         .enter_credentials('invalid_user')
         .click_login()
         )
        print()
