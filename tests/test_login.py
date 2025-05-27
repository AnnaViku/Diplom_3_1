import pytest
import allure
from data.credentials import BASE_URL, TEST_EMAIL, TEST_PASSWORD, INVALID_EMAIL, INVALID_PASSWORD, LOGIN_ERROR_MESSAGE
from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.suite("Авторизация")
@pytest.mark.usefixtures("driver")
class TestLogin:

    @allure.title("Успешная авторизация с валидными данными")
    def test_login_with_valid_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.open(f"{BASE_URL}/login")
        login_page.login(TEST_EMAIL, TEST_PASSWORD)
        main_page = MainPage(driver)
        assert main_page.is_user_logged_in(), "Пользователь не авторизовался после входа"

    @allure.title("Ошибка при авторизации с некорректным email")
    def test_login_with_invalid_email(self, driver):
        login_page = LoginPage(driver)
        login_page.open(f"{BASE_URL}/login")
        login_page.login(INVALID_EMAIL, TEST_PASSWORD)
        assert login_page.is_login_error_displayed(), "Сообщение об ошибке не отображается при неправильном email"

    @allure.title("Ошибка при авторизации с некорректным паролем")
    def test_login_with_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open(f"{BASE_URL}/login")
        login_page.login(TEST_EMAIL, INVALID_PASSWORD)
        assert login_page.is_login_error_displayed(), "Сообщение об ошибке не отображается при неправильном пароле"

    @allure.title("Проверка перехода на форму авторизации с главной страницы")
    def test_navigation_to_login_from_main(self, driver):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.go_to_login()
        assert "login" in driver.current_url, "URL не содержит 'login' после перехода"

    @allure.title("Проверка, что незалогиненный пользователь не может оформить заказ")
    def test_guest_cannot_place_order(self, driver):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.click_order_button()
        assert "login" in driver.current_url, "Незалогиненный пользователь должен быть перенаправлен на страницу логина"
