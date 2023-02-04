from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="add-to-cart-button"]')
    CART_BTN_AFTER_ADD_TO_CART = (By.XPATH, '//*[@id="attach-sidesheet-view-cart-button"]/span/input')
