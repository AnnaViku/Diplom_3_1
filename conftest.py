import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import allure
from data.credentials import BASE_URL, TEST_EMAIL, TEST_PASSWORD
from pages.login_page import LoginPage

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выберите браузер: chrome или firefox"
    )

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1280,800")
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1280")
        options.add_argument("--height=800")
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Браузер {browser} не поддерживается. Используйте chrome или firefox.")

    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def login_user(driver):
    """Фикстура логина через UI"""
    login_page = LoginPage(driver)
    login_page.open(f"{BASE_URL}/login")
    login_page.login(TEST_EMAIL, TEST_PASSWORD)
    yield
