from seleniumPython.pages.base_page import BasePage
from seleniumPython.pages.conversations.conversation_page import ConversationsPage
from seleniumPython.pages.elements.mainSearch import MainSearch
from seleniumPython.pages.elements.navigationBar import NavigationBar
from seleniumPython.pages.loginPage.loginPage import LoginPage
from seleniumPython.pages.search_results.search_results_page import SearchResultsPage


class HomePage(BasePage):
    _navBar = None
    _mainSearch = None

    def __init__(self, driver):
        super().__init__(driver)
        self._navBar = NavigationBar(self.driver)
        self._mainSearch = MainSearch(self.driver)

    def open_page(self):
        self._open("uk/")
        return self

    def open_login_page(self):
        self.navBar.click_on_login_button()
        return LoginPage(self.driver)

    def open_conversations_page(self):
        self.navBar.click_on_conversations_link()
        return ConversationsPage(self.driver)

    def search_for_adds(self, query):
        self._mainSearch.enter_search_query(query)
        self._mainSearch.click_submit_search_button()

        return SearchResultsPage(self.driver)