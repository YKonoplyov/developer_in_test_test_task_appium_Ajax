from .page import Page


class LoginPage(Page):

    def log_in(self, login: str, password: str) -> None:
        to_log_in_page_button = self.find_element_by_text(text="Log In")
        to_log_in_page_button.click()

        email_field = self.find_element_by_id(element_id="authLoginEmail")
        password_field = self.find_element_by_id(element_id="authLoginPassword")
        log_in_button = self.find_element_by_text(text="Log In")

        email_field.send_keys(login)
        password_field.send_keys(password)
        log_in_button.click()
