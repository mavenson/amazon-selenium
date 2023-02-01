from jasamazontests.src.pages.locators.GlobalPageLocators import GlobalPageLocators
from jasamazontests.src.helpers.config_helpers import get_base_url
from jasamazontests.src.SeleniumExtended import SeleniumExtended


class GlobalPage(GlobalPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_homepage(self):
        base_url = get_base_url()
        self.driver.get(base_url)

    def click_shopping_cart(self):
        self.sl.wait_and_click(self.CART_BTN)

