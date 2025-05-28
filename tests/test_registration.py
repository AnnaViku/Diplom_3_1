import pytest
import allure
from data.credentials import BASE_URL
from pages.registration_page import RegistrationPage

@allure.suite("Регистрация")
@pytest.mark.usefixtures("driver")
class TestRegistration:

    @allure.title("Регистрация с валидными данными")
    def test_successful_registration(self, driver):
        page = RegistrationPage(driver)
        page.open(f"{BASE_URL}/register")
        page.register("testuser01", "testuser01@example.com", "SomePass123")
        assert "login" in driver.current_url, "После успешной регистрации не произошло перехода на логин"
