from selenium import webdriver
from pages.order_page import OrderPage
import allure

class TestReturnToMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        cls.order_page = OrderPage(cls.driver)

    @allure.title('Тестирование клика по логотипу Самокат')
    @allure.description('Тест проверяет, что при клике на логотип Самокат происходит возврат на главную страницу')  # Описание теста
    @allure.step('Клик по логотипу Самокат')
    def test_click_on_samokat_logo(self):
        self.test_click_on_samokat_logo()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
