from jasamazontests.src.pages.locators.SearchResultsPageLocators import SearchResultPageLocators
from jasamazontests.src.SeleniumExtended import SeleniumExtended
from selenium.webdriver.common.by import By


class SearchResultsPage(SearchResultPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def click_first_result(self):
        self.sl.wait_and_click(self.FIRST_RESULT)

    def get_results_page_header(self):
#        self.sl.wait_until_element_is_present(By.XPATH, self.RESULTS_HEADER)
        results_header = self.driver.find_element(By.XPATH, self.RESULTS_HEADER).text
        return results_header

    def get_back_to_results_link(self):
#        self.sl.wait_until_element_is_present(By.XPATH, self.SEARCH_QUERY_FROM_RESULT_PRODUCT_PAGE)
        search_query = self.driver.find_element(By.XPATH, self.BACK_TO_RESULTS_LINK).text
        return search_query

