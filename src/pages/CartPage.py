from jasamazontests.src.pages.locators.CartPageLocators import CartPageLocators
from jasamazontests.src.helpers.config_helpers import get_base_url
from jasamazontests.src.SeleniumExtended import SeleniumExtended


class CartPage(CartPageLocators):

    endpoint = 'gp/cart/view.html?ref_=nav_cart'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_cart_page(self):
        base_url = get_base_url()
        cart_url = base_url + self.endpoint
        self.driver.get(cart_url)

    def get_empty_cart_message(self):
        self.sl.wait_until_element_contains_text(self.EMPTY_CART_MESSAGE, "Your Amazon Cart is empty")

