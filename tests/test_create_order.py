from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.about_rent_page import AboutRentPage
from helpers.generators import generate_name_or_surname, generate_address, generate_phone_number
import allure


class TestCreateOrder:

    @allure.title('Тестирование создания заказа с серым цветом самоката')
    @allure.description('Проверка процесса создания заказа с выбором серого цвета самоката')
    @allure.step('Заполнение формы заказа с серым цветом самоката')
    def test_create_order_grey(self, driver):

        name = generate_name_or_surname()
        address = generate_address()
        phone = generate_phone_number()


        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        about_rent_page = AboutRentPage(driver)

        main_page.click_upper_order_button()
        order_page.input_valid_name(name)
        order_page.input_valid_surname(name)
        order_page.input_valid_address(address)
        order_page.input_metro_station()
        order_page.input_valid_phone_number(phone)
        order_page.click_next_button()


        about_rent_page.input_date_through_calendar('25.05.2025')
        about_rent_page.set_the_lease_time(0)
        about_rent_page.set_grey_colour()
        about_rent_page.click_order_button()
        about_rent_page.click_yes_button()

        assert about_rent_page.find_element(about_rent_page.status_button).is_displayed()

    @allure.title('Тестирование создания заказа с черным цветом самоката')
    @allure.description('Проверка процесса создания заказа с выбором черного цвета самоката')
    @allure.step('Заполнение формы заказа с черным цветом самоката')
    def test_create_order_black(self, driver):

        name = generate_name_or_surname()
        address = generate_address()
        phone = generate_phone_number()


        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        about_rent_page = AboutRentPage(driver)


        main_page.click_upper_order_button()
        order_page.input_valid_name(name)
        order_page.input_valid_surname(name)
        order_page.input_valid_address(address)
        order_page.input_metro_station()
        order_page.input_valid_phone_number(phone)
        order_page.click_next_button()


        about_rent_page.input_date_through_calendar('26.06.2025')
        about_rent_page.set_the_lease_time(1)
        about_rent_page.set_black_colour()
        about_rent_page.click_order_button()
        about_rent_page.click_yes_button()

        assert about_rent_page.find_element(about_rent_page.status_button).is_displayed()
