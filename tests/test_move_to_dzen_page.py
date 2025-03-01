from selenium import webdriver
from pages.main_page import MainPage
import allure

class TestMoveDzenPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        cls.main_page = MainPage(cls.driver)

    @allure.title('Тестирование открытия страницы Дзена при клике на логотип')
    @allure.description('Проверяется, что при клике на логотип происходит переход на страницу Дзена')
    @allure.step('Клик по логотипу для перехода на страницу Дзена')
    def test_open_dzen_page(self):
        self.main_page.click_on_logo()
        current_url = self.driver.current_url
        assert current_url == 'https://dzen.ru/?yredirect=true'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
