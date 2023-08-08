from .base_test import BaseTest
from seleniumPython.pages.homePage.homePage import HomePage
from ..pages.account.account_page import AccountPage


class LoginTest(BaseTest):

    def testLogin(self):
        home_page = HomePage(self.driver)
        (home_page
         .open_page()
         .open_login_page()
         .enter_credentials('my')
         .click_login()
         )
        page_title = AccountPage(self.driver).get_header_title()
        assert page_title == 'Ваші оголошення'
