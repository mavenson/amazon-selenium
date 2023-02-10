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
        url = home_page.get_homepage_url()
        assert url == 'https://www.amazon.com/'

        # type search query
        query = 'hello kitty'
        search_bar.enter_text_in_search_bar(query)

        # click search and check if on results page
        search_bar.click_search_button()
        result_page_header = results_page.get_results_page_header()
        print(result_page_header)
        assert result_page_header == 'RESULTS'

        # click first result and check if on result product page
        results_page.click_first_result()
        result_page_query = results_page.get_back_to_results_link()
        assert result_page_query == 'Back to results'
