from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProfilePage(BasePage):
    PROFILE_LINK = (By.LINK_TEXT, "Личный Кабинет")
    ORDER_HISTORY = (By.LINK_TEXT, "История заказов")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    def go_to_profile(self):
        self.click(self.PROFILE_LINK)

    def go_to_order_history(self):
        self.click(self.ORDER_HISTORY)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
