import pytest
from jasamazontests.src.site.CartButton import CartButton
from jasamazontests.src.pages.HomePage import HomePage
from jasamazontests.src.pages.CartPage import CartPage
from jasamazontests.src.pages.ProductPage import ProductPage

@pytest.mark.usefixtures("init_driver")
class TestAddCartButton:

    @pytest.mark.tcid01
    def test_add_cart_button(self):
        # CART SHOULD BE EMPTY BEFORE RUNNING
        home_page = HomePage(self.driver)
        cart_page = CartPage(self.driver)
        product_page = ProductPage(self.driver)
        cart_button = CartButton(self.driver)

        # go to home page
        home_page.go_to_homepage()
        homepage_url = home_page.get_homepage_url()
        assert homepage_url == 'https://www.amazon.com/'

        # click on shopping cart and check if empty
        cart_button.click_shopping_cart()
        empty_cart_message = cart_page.get_empty_cart_message()
        assert empty_cart_message == 'Your Amazon Cart is empty'

        # go to some product page
        product_page_url = homepage_url + 'Amazon-Basics-Lightweight-Microfiber-14-Inch/dp/B06X9PS779?ref_=ast_sto_dp&th=1&psc=1'
        product_page.go_to_product_page()
        curr_url = product_page.get_product_page_url()
        assert curr_url == product_page_url

        # click add to cart button and go to cart
        product_page.click_add_to_cart()
        product_page.click_cart_after_add_to_cart()
        items_in_cart = product_page.get_number_products_in_cart()
        assert items_in_cart == '1'

        # check if cart contains an item (header does not appear otherwise)
        cart_header = cart_page.get_shopping_cart_header()
        assert cart_header == 'Shopping Cart'
