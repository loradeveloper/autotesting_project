import sys
import os

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from utils.data_generators import generate_random_email, generate_random_strong_password


@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = generate_random_email()
        password = generate_random_strong_password()
        page.register_new_user(email, password)
        page.should_be_authorized_user()


    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.check_message_about_item_in_basket()
        page.check_basket_price_message()


    def test_user_cant_see_success_message(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.parametrize('promo_offer', [0, 1, 2, 3, 4, 5, 6,
                                         pytest.param(7, marks=pytest.mark.xfail),
                                         8, 9])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.check_message_about_item_in_basket()
    page.check_basket_price_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_basket_is_empty()
    basket_page.should_be_message_about_basket_is_empty()
