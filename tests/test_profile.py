import pytest
import allure
from data.credentials import BASE_URL, TEST_EMAIL, TEST_PASSWORD
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

@allure.suite("Личный кабинет")
@pytest.mark.usefixtures("driver")
class TestProfile:

    @allure.title("Переход по клику на 'Личный кабинет'")
    def test_go_to_profile(self, driver):
        login = LoginPage(driver)
        login.open(f"{BASE_URL}/login")
        login.login(TEST_EMAIL, TEST_PASSWORD)
        profile = ProfilePage(driver)
        profile.go_to_profile()
        assert "account/profile" in driver.current_url

    @allure.title("Переход в раздел 'История заказов'")
    def test_go_to_order_history(self, driver):
        login = LoginPage(driver)
        login.open(f"{BASE_URL}/login")
        login.login(TEST_EMAIL, TEST_PASSWORD)
        profile = ProfilePage(driver)
        profile.go_to_order_history()
        assert "account/orders" in driver.current_url

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver):
        login = LoginPage(driver)
        login.open(f"{BASE_URL}/login")
        login.login(TEST_EMAIL, TEST_PASSWORD)
        profile = ProfilePage(driver)
        profile.logout()
        assert "login" in driver.current_url
