import allure
import pytest
from data.credentials import BASE_URL, TEST_EMAIL
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

@allure.suite("Восстановление пароля")
@pytest.mark.usefixtures("driver")
class TestForgotPassword:

    @allure.title("Переход на страницу восстановления пароля")
    def test_forgot_password_navigation(self, driver):
        login = LoginPage(driver)
        login.open(f"{BASE_URL}/login")
        login.go_to_forgot_password()
        assert "forgot-password" in driver.current_url

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_forgot_password_submit(self, driver):
        forgot = ForgotPasswordPage(driver)
        forgot.open(f"{BASE_URL}/forgot-password")
        forgot.restore_password(TEST_EMAIL)

    @allure.title("Кнопка показать/скрыть пароль активирует поле")
    def test_password_field_becomes_active(self, driver):
        forgot = ForgotPasswordPage(driver)
        forgot.open(f"{BASE_URL}/forgot-password")
        forgot.toggle_password_visibility()
        active = forgot.get_active_element()
        assert active == forgot.get_element(ForgotPasswordPage.EMAIL_INPUT)


