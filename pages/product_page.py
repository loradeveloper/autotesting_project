import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket.click()
        # self.solve_quiz_and_get_code()

    def check_message_about_item_in_basket(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME_H1).text
        item_name_in_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_ITEM_NAME_DIV).text
        assert item_name == item_name_in_basket, "Item name doesn't match item name in basket"

    def check_basket_price_message(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_P).text
        basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert item_price in basket_total_price, "Item price doesn't match basket total price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_DIV), \
            "Success message is presented, but should not be"


    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_DIV), \
            "Success message is not disappeared, but should be"
