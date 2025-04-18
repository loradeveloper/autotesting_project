from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href$='/password-reset/']")
    LOGIN_LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    REGISTER_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div[class='alertinner wicon']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
    ITEM_NAME_H1 = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_WITH_ITEM_NAME_DIV = (By.CSS_SELECTOR, "#messages div[class='alert alert-safe alert-noicon alert-success  fade in'] div.alertinner strong")
    SUCCESS_MESSAGE_DIV = (By.CSS_SELECTOR, "#messages div[class='alert alert-safe alert-noicon alert-success  fade in'] div.alertinner strong")
    ITEM_PRICE_P = (By.CSS_SELECTOR, "div.product_main p.price_color")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, "header div.basket-mini:nth-child(2)")


class BasketPageLocators:
    GO_TO_BASKET_PAGE_LINK = (By.CSS_SELECTOR, "span.btn-group a[class='btn btn-default']")
    BASKET_EMPTY_MESSAGE_P = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_SUMMARY_FORM = (By.CSS_SELECTOR, "#basket_formset")
