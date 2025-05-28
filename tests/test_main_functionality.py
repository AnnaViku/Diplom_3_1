import pytest
import allure
from data.credentials import BASE_URL, TEST_EMAIL, TEST_PASSWORD
from pages.main_page import MainPage
from pages.login_page import LoginPage

@allure.suite("Проверка основного функционала")
@pytest.mark.usefixtures("driver")
class TestMainFunctionality:

    @allure.title("Переход на страницу 'Конструктор'")
    def test_go_to_constructor(self, driver):
        main = MainPage(driver)
        main.open(BASE_URL)
        main.go_to_constructor()
        assert "constructor" in main.get_current_url()

    @allure.title("Переход на страницу 'Лента заказов'")
    def test_go_to_order_feed(self, driver):
        main = MainPage(driver)
        main.open(BASE_URL)
        main.go_to_order_feed()
        assert "feed" in main.get_current_url()

    @allure.title("Открытие всплывающего окна с деталями ингредиента")
    def test_open_ingredient_modal(self, driver):
        main = MainPage(driver)
        main.open(BASE_URL)
        main.open_ingredient_details()
        assert main.is_element_visible((MainPage.POPUP_CLOSE))

    @allure.title("Закрытие всплывающего окна с ингредиентом")
    def test_close_ingredient_modal(self, driver):
        main = MainPage(driver)
        main.open(BASE_URL)
        main.open_ingredient_details()
        main.close_popup()
        assert not main.is_element_visible((MainPage.POPUP_CLOSE))

    @allure.title("Увеличение счётчика ингредиента при добавлении")
    def test_ingredient_counter_increase(self, driver):
        main = MainPage(driver)
        main.open(BASE_URL)
        main.open_ingredient_details()
        counter_before = int(main.get_ingredient_counter())
        main.open_ingredient_details()
        counter_after = int(main.get_ingredient_counter())
        assert counter_after == counter_before + 1

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_authenticated_user_can_order(self, driver):
        login = LoginPage(driver)
        login.open(f"{BASE_URL}/login")
        login.login(TEST_EMAIL, TEST_PASSWORD)
        main = MainPage(driver)
        main.click_order_button()
        assert "order" in main.get_current_url()
