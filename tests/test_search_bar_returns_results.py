import pytest
from jasamazontests.src.site.SearchBar import SearchBar
from jasamazontests.src.pages.HomePage import HomePage
from jasamazontests.src.pages.SearchResultsPage import SearchResultsPage


@pytest.mark.usefixtures('init_driver')
class TestSearchBarReturnsResults:

    @pytest.mark.tcid02
    def test_search_bar_returns_results(self):
        home_page = HomePage(self.driver)
        search_bar = SearchBar(self.driver)
        results_page = SearchResultsPage(self.driver)

        # go to home page
        home_page.go_to_homepage()

        # type search query
        search_bar.enter_text_in_search_bar('hello kitty')

        # click search
        search_bar.click_search_button()

        # first result exists
        results_page.click_first_result()

