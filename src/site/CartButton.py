from jasamazontests.src.SeleniumExtended import SeleniumExtended
from jasamazontests.src.site.locators.CartButtonLocators import CartButtonLocators


class CartButton(CartButtonLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def click_shopping_cart(self):
        self.sl.wait_and_click(self.CART_BTN)



