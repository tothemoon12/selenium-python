from selenium.webdriver.common.by import By

from seleniumPython.pages.base_page import BasePage
from seleniumPython.pages.elements.mainSearch import MainSearch


class SearchResultsPage(BasePage):
    _LISTING_COUNT_MSG_LOCATOR = (By.XPATH, '//span[@data-testid="total-count"]')
    _mainSearch = None

    def __init__(self, driver):
        super().__init__(driver)
        self._mainSearch = MainSearch(self.driver)

    def get_results_count(self):
        text = str(self._find_element(*self._LISTING_COUNT_MSG_LOCATOR).text)
        return int(text.split(' ')[2])
