from pages.order_page import OrderPage
import allure

class TestReturnToMainPage:


    @allure.title('Тестирование клика по логотипу Самокат')
    @allure.description('Тест проверяет, что при клике на логотип Самокат происходит возврат на главную страницу')  # Описание теста
    @allure.step('Клик по логотипу Самокат')
    def test_click_on_samokat_logo(self, driver):
        order_page = OrderPage(driver)

        order_page.click_samokat_logo()

        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"
