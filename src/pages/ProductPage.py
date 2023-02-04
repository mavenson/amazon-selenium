from jasamazontests.src.pages.locators.ProductPageLocators import ProductPageLocators
from jasamazontests.src.helpers.config_helpers import get_base_url
from jasamazontests.src.SeleniumExtended import SeleniumExtended


class ProductPage(ProductPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_product_page(self, endpoint):
        base_url = get_base_url()
        product_page_url = base_url + endpoint
        self.driver.get(product_page_url)

    def click_add_to_cart(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BUTTON)

    def click_cart_after_add_to_cart(self):
        self.sl.wait_and_click(self.CART_BTN_AFTER_ADD_TO_CART)