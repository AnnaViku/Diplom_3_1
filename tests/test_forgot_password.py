import pytest
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

@pytest.mark.usefixtures("driver")
def test_forgot_password_navigation(driver):
    login = LoginPage(driver)
    login.open("https://stellarburgers.nomoreparties.site/login")
    login.go_to_forgot_password()
    assert "forgot-password" in driver.current_url

@pytest.mark.usefixtures("driver")
def test_forgot_password_submit(driver):
    login = LoginPage(driver)
    login.open("https://stellarburgers.nomoreparties.site/login")
    login.go_to_forgot_password()
    forgot = ForgotPasswordPage(driver)
    forgot.restore_password("user@example.com")
    # предполагаем, что после отправки формы происходит редирект или уведомление
    assert driver.current_url.endswith("/reset-password") or "отправлено" in driver.page_source

@pytest.mark.usefixtures("driver")
def test_forgot_password_field_focus(driver):
    login = LoginPage(driver)
    login.open("https://stellarburgers.nomoreparties.site/login")
    login.go_to_forgot_password()
    forgot = ForgotPasswordPage(driver)
    forgot.toggle_password_visibility()
    input_field = forgot.get_element(ForgotPasswordPage.EMAIL_INPUT)
    assert input_field == driver.switch_to.active_element


# tests/test_profile.py
import pytest
from pages.main_page import MainPage
from pages.profile_page import ProfilePage

@pytest.mark.usefixtures("driver")
def test_profile_navigation(driver):
    main = MainPage(driver)
    main.open("https://stellarburgers.nomoreparties.site")
    profile = ProfilePage(driver)
    profile.go_to_profile()
    assert "profile" in driver.current_url

@pytest.mark.usefixtures("driver")
def test_order_history_access(driver):
    profile = ProfilePage(driver)
    profile.open("https://stellarburgers.nomoreparties.site/profile")
    profile.go_to_order_history()
    assert "orders" in driver.current_url

@pytest.mark.usefixtures("driver")
def test_logout(driver):
    profile = ProfilePage(driver)
    profile.open("https://stellarburgers.nomoreparties.site/profile")
    profile.logout()
    assert "login" in driver.current_url


# tests/test_main_functionality.py
import pytest
from pages.main_page import MainPage

@pytest.mark.usefixtures("driver")
def test_constructor_navigation(driver):
    main = MainPage(driver)
    main.open("https://stellarburgers.nomoreparties.site")
    main.click(MainPage.CONSTRUCTOR_BUTTON)
    assert "constructor" in driver.current_url or "bun" in driver.page_source

@pytest.mark.usefixtures("driver")
def test_order_feed_navigation(driver):
    main = MainPage(driver)
    main.open("https://stellarburgers.nomoreparties.site")
    main.click(MainPage.ORDER_FEED_BUTTON)
    assert "feed" in driver.current_url

@pytest.mark.usefixtures("driver")
def test_ingredient_modal(driver):
    main = MainPage(driver)
    main.open("https://stellarburgers.nomoreparties.site")
    main.open_ingredient_details()
    assert "детали ингредиента" in driver.page_source.lower()
    main.close_popup()
    assert "детали ингредиента" not in driver.page_source.lower()

@pytest.mark.usefixtures("driver")
def test_ingredient_counter_increment(driver):
    main = MainPage(driver)
    main.open("https://stellarburgers.nomoreparties.site")
    count_before = len(driver.find_elements(*MainPage.INGREDIENT_COUNTER))
    main.open_ingredient_details()
    main.click((By.XPATH, "//button[text()='Добавить']"))
    count_after = len(driver.find_elements(*MainPage.INGREDIENT_COUNTER))
    assert count_after > count_before

@pytest.mark.usefixtures("driver")
def test_logged_user_can_order(driver):
    # Залогиниться можно через precondition или напрямую через UI
    main = MainPage(driver)
    main.open("https://stellarburgers.nomoreparties.site")
    main.click((By.XPATH, "//button[text()='Оформить заказ']"))
    assert "order-details" in driver.current_url or "номер заказа" in driver.page_source.lower()


# tests/test_orders_feed.py
import pytest
from pages.orders_feed_page import OrdersFeedPage

@pytest.mark.usefixtures("driver")
def test_order_details_popup(driver):
    orders = OrdersFeedPage(driver)
    orders.open("https://stellarburgers.nomoreparties.site/feed")
    orders.open_order_details()
    assert "информация о заказе" in driver.page_source.lower()

@pytest.mark.usefixtures("driver")
def test_user_orders_in_feed(driver):
    orders = OrdersFeedPage(driver)
    orders.open("https://stellarburgers.nomoreparties.site/feed")
    assert len(driver.find_elements(*OrdersFeedPage.ORDER_ITEM)) > 0

@pytest.mark.usefixtures("driver")
def test_total_completed_counter(driver):
    orders = OrdersFeedPage(driver)
    orders.open("https://stellarburgers.nomoreparties.site/feed")
    total_elem = orders.get_element(OrdersFeedPage.TOTAL_COMPLETED)
    assert total_elem.text.isdigit()

@pytest.mark.usefixtures("driver")
def test_today_completed_counter(driver):
    orders = OrdersFeedPage(driver)
    orders.open("https://stellarburgers.nomoreparties.site/feed")
    today_elem = orders.get_element(OrdersFeedPage.COMPLETED_TODAY)
    assert today_elem.text.isdigit()

@pytest.mark.usefixtures("driver")
def test_order_in_work_appears(driver):
    orders = OrdersFeedPage(driver)
    orders.open("https://stellarburgers.nomoreparties.site/feed")
    assert len(driver.find_elements(*OrdersFeedPage.IN_PROGRESS)) > 0