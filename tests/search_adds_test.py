from seleniumPython.pages.homePage.homePage import HomePage
from seleniumPython.tests.base_test import BaseTest


class SearchAddsTest(BaseTest):

    def test_search_for_item(self):
        search_query = "NBT Evo"

        page = (HomePage(self.driver)
                .open_page()
                .search_for_adds(search_query)
                )

        current_url = str(page.get_url())
        url_query = current_url.split("/")

        assert url_query[-2].endswith(search_query.replace(" ", "-"))
        assert page.get_results_count() >= 0
