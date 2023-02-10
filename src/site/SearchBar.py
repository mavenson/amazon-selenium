from jasamazontests.src.SeleniumExtended import SeleniumExtended
from jasamazontests.src.site.locators.SearchBarLocators import SearchBarLocators


class SearchBar(SearchBarLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def enter_text_in_search_bar(self, text):
        self.sl.wait_and_send_text(self.SEARCH_BAR, text)

    def click_search_button(self):
        self.sl.wait_and_click(self.SEARCH_BUTTON)

