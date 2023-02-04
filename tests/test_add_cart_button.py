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

        # click on shopping cart
        cart_button.click_shopping_cart()

        # check if cart is empty
        cart_page.get_empty_cart_message()

        # go to some product page
        product_page.go_to_product_page('Amazon-Basics-Lightweight-Microfiber-14-Inch/dp/B06X9PS779?ref_=ast_sto_dp&th=1&psc=1')

        # click add to cart button
        product_page.click_add_to_cart()

        # go to cart page
        product_page.click_cart_after_add_to_cart()