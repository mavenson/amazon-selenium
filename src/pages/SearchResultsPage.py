from jasamazontests.src.pages.locators.SearchResultsPageLocators import SearchResultPageLocators
from jasamazontests.src.SeleniumExtended import SeleniumExtended


class SearchResultsPage(SearchResultPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def click_first_result(self):
        first_result = self.sl.wait_and_click(self.FIRST_RESULT)