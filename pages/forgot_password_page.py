import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ForgotPasswordPage(BasePage):
    EMAIL_INPUT = (By.NAME, "name")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_TOGGLE = (By.CLASS_NAME, "input__icon")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "forgot-password__success")

    @allure.step("Ввод почты и отправка формы восстановления")
    def restore_password(self, email):
        self.fill(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_BUTTON)

    @allure.step("Нажатие кнопки показать/скрыть пароль")
    def toggle_password_visibility(self):
        self.click(self.PASSWORD_TOGGLE)

    @allure.step("Получение текста подтверждения восстановления пароля")
    def get_success_message_text(self):
        return self.get_element(self.SUCCESS_MESSAGE).text
