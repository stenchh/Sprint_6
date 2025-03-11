import allure
from pages.main_page import MainPage

class TestMoveDzenPage:

    @allure.title('Тестирование открытия страницы Дзена при клике на логотип')
    @allure.description('Проверяется, что при клике на логотип происходит переход на страницу Дзена')
    @allure.step('Клик по логотипу для перехода на страницу Дзена')
    def test_open_dzen_page(self, driver):
        main_page = MainPage(driver)

        current_url = main_page.click_on_logo()

        assert current_url == 'https://dzen.ru/?yredirect=true'