from selenium.webdriver.common.by import By


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
