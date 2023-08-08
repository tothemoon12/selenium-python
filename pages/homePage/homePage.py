from seleniumPython.pages.base_page import BasePage
from seleniumPython.pages.conversations.conversation_page import ConversationsPage
from seleniumPython.pages.elements.navigationBar import NavigationBar
from seleniumPython.pages.loginPage.loginPage import LoginPage


class HomePage(BasePage):
    navBar = None

    def __init__(self, driver):
        super().__init__(driver)
        # self.open("uk/")
        self.navBar = NavigationBar(self.driver)

    def open_login_page(self):
        self.navBar.click_on_login_button()
        return LoginPage(self.driver)


    def open_conversations_page(self):
        self.navBar.click_on_conversations_link()
        return ConversationsPage(self.driver)