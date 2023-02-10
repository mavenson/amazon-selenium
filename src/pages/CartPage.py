from jasamazontests.src.pages.locators.CartPageLocators import CartPageLocators
from jasamazontests.src.helpers.config_helpers import get_base_url
from jasamazontests.src.SeleniumExtended import SeleniumExtended
from selenium.webdriver.common.by import By


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
        empty_cart_message = self.driver.find_element(By.XPATH, '//*[@id="sc-active-cart"]/div/div/div[2]/div[1]/h2').text
        return empty_cart_message

    def get_shopping_cart_header(self):
        cart_header = self.driver.find_element(By.XPATH, '//*[@id="sc-active-cart"]/div/div/div/h1').text
        return cart_header

