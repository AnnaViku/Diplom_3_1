import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу по адресу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввод значения '{value}' в поле {locator}")
    def fill(self, locator, value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    @allure.step("Получение элемента {locator}")
    def get_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Получение активного элемента")
    def get_active_element(self):
        return self.driver.switch_to.active_element

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

