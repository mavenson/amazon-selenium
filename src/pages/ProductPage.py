from jasamazontests.src.pages.locators.ProductPageLocators import ProductPageLocators
from jasamazontests.src.helpers.config_helpers import get_base_url


class ProductPage(ProductPageLocators):

    def __init__(self, driver):
        self.driver = driver

    def go_to_product_page(self, endpoint):
        base_url = get_base_url()
        product_page_url = base_url + endpoint
        self.driver.get(product_page_url)