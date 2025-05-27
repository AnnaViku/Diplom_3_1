import pytest
import allure
from data.credentials import BASE_URL
from pages.orders_feed_page import OrdersFeedPage

@allure.suite("Лента заказов")
@pytest.mark.usefixtures("driver")
class TestOrdersFeed:

    @allure.title("Открытие деталей заказа из ленты заказов")
    def test_open_order_details(self, driver):
        feed = OrdersFeedPage(driver)
        feed.open(f"{BASE_URL}/feed")
        feed.open_order_details()
        assert feed.is_element_visible((OrdersFeedPage.ORDER_ITEM))

    @allure.title("Увеличение счётчика 'Выполнено за всё время' после создания заказа")
    def test_total_completed_increases(self, driver):
        feed = OrdersFeedPage(driver)
        feed.open(f"{BASE_URL}/feed")
        before = feed.get_total_completed()
        # Здесь должен быть вызов API или UI для создания нового заказа
        # simulate_order_creation()
        after = feed.get_total_completed()
        assert after > before

    @allure.title("Увеличение счётчика 'Выполнено за сегодня' после создания заказа")
    def test_completed_today_increases(self, driver):
        feed = OrdersFeedPage(driver)
        feed.open(f"{BASE_URL}/feed")
        before = feed.get_completed_today()
        # simulate_order_creation()
        after = feed.get_completed_today()
        assert after > before

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_number_in_in_progress(self, driver):
        feed = OrdersFeedPage(driver)
        feed.open(f"{BASE_URL}/feed")
        order_number = "123456"  # Должно быть получено после создания заказа
        assert feed.is_order_in_progress(order_number)
