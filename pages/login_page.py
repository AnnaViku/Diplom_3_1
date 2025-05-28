import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'Некорректный email или пароль')]")

    @allure.step("Ввод email: {email} и пароля, отправка формы")
    def login(self, email, password):
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    @allure.step("Проверка наличия ошибки авторизации")
    def is_login_error_displayed(self):
        return self.is_visible(self.ERROR_MESSAGE)
