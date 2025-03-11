from pages.order_page import OrderPage
from pages.main_page import MainPage
import allure

class TestReturnToMainPage:


    @allure.title('Тестирование клика по логотипу Самокат')
    @allure.description('Тест проверяет, что при клике на логотип Самокат происходит возврат на главную страницу со страницы Заказа')
    @allure.step('Клик по логотипу Самокат')
    def test_click_on_samokat_logo(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.click_lower_order_button()


        current_url = order_page.click_samokat_logo()

        assert current_url == "https://qa-scooter.praktikum-services.ru/"
