from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")

    def go_to_forgot_password(self):
        self.click(self.FORGOT_PASSWORD_LINK)
