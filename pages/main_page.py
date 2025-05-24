from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор")
    ORDER_FEED_BUTTON = (By.LINK_TEXT, "Лента заказов")
    INGREDIENT = (By.CLASS_NAME, "burger-ingredient")
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter")
    POPUP_CLOSE = (By.CLASS_NAME, "Modal_close__3CGYF")

    def open_ingredient_details(self):
        self.click(self.INGREDIENT)

    def close_popup(self):
        self.click(self.POPUP_CLOSE)
