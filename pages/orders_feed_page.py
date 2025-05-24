from selenium.webdriver.common.by import By
from .base_page import BasePage

class OrdersFeedPage(BasePage):
    ORDER_ITEM = (By.CLASS_NAME, "order-card")
    TOTAL_COMPLETED = (By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p")
    COMPLETED_TODAY = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")
    IN_PROGRESS = (By.CLASS_NAME, "OrderFeed_listReady__2xqac")

    def open_order_details(self):
        self.click(self.ORDER_ITEM)
