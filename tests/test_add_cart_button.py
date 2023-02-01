import pytest
from jasamazontests.src.pages.CartPage import CartPage
from jasamazontests.src.pages.GlobalPage import GlobalPage


@pytest.mark.usefixtures("init_driver")
class TestAddCartButton:

    @pytest.mark.tcid01
    def test_add_cart_button(self):
        # CART SHOULD BE EMPTY BEFORE RUNNING
        global_page = GlobalPage(self.driver)
        cart_page = CartPage(self.driver)

        # go to home page
        global_page.go_to_homepage()

        # click on shopping cart
        global_page.click_shopping_cart()

        # check if cart is empty
        cart_page.get_empty_cart_message()

        # go to some product page

        # click add to cart button

        # verify is on cart page

        # get number of items in cart

        # verify items in cart is one more than before
