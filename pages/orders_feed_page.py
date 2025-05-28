import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class OrdersFeedPage(BasePage):
    ORDER_ITEM = (By.CLASS_NAME, "order-card")
    TOTAL_COMPLETED = (By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p")
    COMPLETED_TODAY = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")
    IN_PROGRESS = (By.CLASS_NAME, "OrderFeed_listReady__2xqac")

    @allure.step("Открытие деталей заказа")
    def open_order_details(self):
        self.click(self.ORDER_ITEM)

    @allure.step("Получение количества заказов 'Выполнено за всё время'")
    def get_total_completed(self):
        return int(self.get_element(self.TOTAL_COMPLETED).text)

    @allure.step("Получение количества заказов 'Выполнено за сегодня'")
    def get_completed_today(self):
        return int(self.get_element(self.COMPLETED_TODAY).text)

    @allure.step("Проверка наличия заказа в блоке 'В работе'")
    def is_order_in_progress(self, order_number: str) -> bool:
        progress_block = self.get_element(self.IN_PROGRESS).text
        return order_number in progress_block
