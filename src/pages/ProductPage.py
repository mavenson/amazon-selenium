from jasamazontests.src.pages.locators.ProductPageLocators import ProductPageLocators
from jasamazontests.src.helpers.config_helpers import get_base_url, get_current_url
from jasamazontests.src.SeleniumExtended import SeleniumExtended
from selenium.webdriver.common.by import By

class ProductPage(ProductPageLocators):

    endpoint = 'Amazon-Basics-Lightweight-Microfiber-14-Inch/dp/B06X9PS779?ref_=ast_sto_dp&th=1&psc=1'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_product_page(self):
        base_url = get_base_url()
        product_page_url = base_url + self.endpoint
        self.driver.get(product_page_url)

    def click_add_to_cart(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BUTTON)

    def click_cart_after_add_to_cart(self):
        self.sl.wait_and_click(self.CART_BTN_AFTER_ADD_TO_CART)

    def get_product_page_url(self):
        return get_current_url(self.driver)

    def get_number_products_in_cart(self):
        number_in_cart = self.driver.find_element(By.XPATH, self.SHOPPING_CART_ITEMS_COUNT).text
        return number_in_cart
