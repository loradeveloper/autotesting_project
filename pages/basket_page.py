from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY_FORM), \
            "Basket is not empty, but should be"


    def should_be_message_about_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE_P), \
            "Message about empty basket is not presented, but should be"
