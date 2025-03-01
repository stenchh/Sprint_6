from selenium import webdriver
from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.about_rent_page import AboutRentPage
import allure

class TestCreateOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        cls.order_page = OrderPage(cls.driver)
        cls.main_page = MainPage(cls.driver)
        cls.about_rent_page = AboutRentPage(cls.driver)

    @allure.title('Тестирование создания заказа с серым цветом самоката')
    @allure.description('Проверка процесса создания заказа с выбором серого цвета самоката')
    @allure.step('Заполнение формы заказа с серым цветом самоката')
    def test_create_order_grey(self, generate_name_or_surname, generate_address, generate_phone_number):
        self.main_page.click_upper_order_button()
        self.order_page.input_valid_name(generate_name_or_surname)
        self.order_page.input_valid_surname(generate_name_or_surname)
        self.order_page.input_valid_address(generate_address)
        self.order_page.input_metro_station()
        self.order_page.input_valid_phone_number(generate_phone_number)
        self.order_page.click_next_button()

        self.about_rent_page.input_date_through_caledar1()
        self.about_rent_page.set_the_lease_time()
        self.about_rent_page.set_grey_colour()
        self.about_rent_page.click_order_button()
        self.about_rent_page.click_yes_button()

    @allure.title('Тестирование создания заказа с черным цветом самоката')
    @allure.description('Проверка процесса создания заказа с выбором черного цвета самоката')
    @allure.step('Заполнение формы заказа с черным цветом самоката')
    def create_order_black(self, generate_name_or_surname, generate_address, generate_phone_number):
        self.main_page.click_upper_order_button()
        self.order_page.input_valid_name(generate_name_or_surname)
        self.order_page.input_valid_surname(generate_name_or_surname)
        self.order_page.input_valid_address(generate_address)
        self.order_page.input_metro_station()
        self.order_page.input_valid_phone_number(generate_phone_number)
        self.order_page.click_next_button()

        self.about_rent_page.input_date_through_caledar2()
        self.about_rent_page.set_the_lease_time()
        self.about_rent_page.set_black_colour()
        self.about_rent_page.click_order_button()
        self.about_rent_page.click_yes_button()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
