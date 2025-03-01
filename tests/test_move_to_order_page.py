from selenium import webdriver
from pages.main_page import MainPage
import allure

class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        cls.main_page = MainPage(cls.driver)

    @allure.title('Тестирование перехода на страницу заказа через верхнюю кнопку')
    @allure.description('Проверяется, что при клике на верхнюю кнопку происходит переход на страницу заказа')
    @allure.step('Клик по верхней кнопке заказа')
    def test_move_to_order_page_upper_button(self):
        self.main_page.click_upper_order_button()
        current_url = self.driver.current_url
        assert current_url == 'https://qa-scooter.praktikum-services.ru/order'

    @allure.title('Тестирование перехода на страницу заказа через нижнюю кнопку')
    @allure.description('Проверяется, что при клике на нижнюю кнопку происходит переход на страницу заказа')
    @allure.step('Клик по нижней кнопке заказа')
    def test_move_to_order_page_lower_button(self):
        self.main_page.click_lower_order_button()
        current_url = self.driver.current_url
        assert current_url == 'https://qa-scooter.praktikum-services.ru/order'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
