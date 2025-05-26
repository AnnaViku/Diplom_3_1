from selenium.webdriver.common.by import By
from .base_page import BasePage

class ForgotPasswordPage(BasePage):
    EMAIL_INPUT = (By.NAME, "name")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_TOGGLE = (By.CLASS_NAME, "input__icon")

    def restore_password(self, email):
        self.fill(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_BUTTON)

    def toggle_password_visibility(self):
        self.click(self.PASSWORD_TOGGLE)
