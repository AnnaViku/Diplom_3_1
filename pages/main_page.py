import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    PROFILE_ICON = (By.CLASS_NAME, "AppHeader_header__link__3D_hX")  # иконка профиля
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    @allure.step("Проверка, авторизован ли пользователь (иконка профиля)")
    def is_user_logged_in(self):
        return self.is_visible(self.PROFILE_ICON)

    @allure.step("Переход к авторизации через кнопку")
    def go_to_login(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step("Нажатие кнопки 'Оформить заказ'")
    def click_order_button(self):
        self.click(self.ORDER_BUTTON)
