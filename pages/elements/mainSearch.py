from selenium.webdriver.common.by import By

from seleniumPython.pages.base_page import BasePage


class MainSearch(BasePage):
    _SEARCH_CONTAINER_LOCATOR = (By.ID, 'searchmain')
    _SEARCH_INPUT_LOCATOR = (By.ID, 'headerSearch')
    _SUBMIT_BUTTON_LOCATOR = (By.ID, 'submit-searchmain')

    def enter_search_query(self, query):
        self._wait_element(*self._SEARCH_CONTAINER_LOCATOR)
        self._wait_element(*self._SEARCH_INPUT_LOCATOR)
        self._find_element(*self._SEARCH_INPUT_LOCATOR).send_keys(query)

    def click_submit_search_button(self):
        self._find_element(*self._SUBMIT_BUTTON_LOCATOR).click()