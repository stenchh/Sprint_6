from pages.main_page import MainPage
import allure

class TestOrderPage:

    @allure.title('Тестирование перехода на страницу заказа через верхнюю кнопку')
    @allure.description('Проверяется, что при клике на верхнюю кнопку происходит переход на страницу заказа')
    @allure.step('Клик по верхней кнопке заказа и проверка перехода')
    def test_move_to_order_page_upper_button(self, driver):
        main_page = MainPage(driver)
        current_url = main_page.click_upper_order_button()

        assert current_url == "https://qa-scooter.praktikum-services.ru/order"
    @allure.title('Тестирование перехода на страницу заказа через нижнюю кнопку')
    @allure.description('Проверяется, что при клике на нижнюю кнопку происходит переход на страницу заказа')
    @allure.step('Клик по нижней кнопке заказа и проверка перехода')
    def test_move_to_order_page_lower_button(self, driver):
        main_page = MainPage(driver)
        current_url = main_page.click_lower_order_button()

        current_url == "https://qa-scooter.praktikum-services.ru/order"