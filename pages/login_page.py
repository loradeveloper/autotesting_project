from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_link_fit("login"), "Invalid login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        password_input.send_keys(password)

        confirm_password_input = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_REGISTER_BUTTON)
        register_button.click()

        assert "login" not in self.browser.current_url and self.is_element_present(*LoginPageLocators.REGISTER_SUCCESS_MESSAGE), \
            ("New user registration is failed"
             "PROBABLY email is not unique"
             "Try again")

