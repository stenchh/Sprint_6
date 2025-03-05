import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.about_rent_page import AboutRentPage


class OrderPage(BasePage):
    name_input = [By.XPATH, "//input[@placeholder='* Имя']"]
    surname_input = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address_input = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    number_input = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    button_next = [By.XPATH, "//button[text()='Далее']"]
    logo_samokat = [By.XPATH, "//*[@id='root']/div/div[1]/div[1]/a[2]/img"]
    metro_input = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    metro_select = [By.XPATH, "//*[@class='select-search__select']"]

    def __init__(self, driver):
        super().__init__(driver)
        self.about_rent_page = AboutRentPage(driver)

    @allure.step('Ввод имени')
    def input_valid_name(self, name):
        self.input_text(self.name_input, name)

    @allure.step('Ввод фамилии')
    def input_valid_surname(self, surname):
        self.input_text(self.surname_input, surname)

    @allure.step('Ввод адреса доставки')
    def input_valid_address(self, address):
        self.input_text(self.address_input, address)

    @allure.step('Ввод станции метро')
    def input_metro_station(self):
        self.input_text(self.metro_input, 'Полянка')
        self.wait_until_visible(self.metro_select)
        self.click_element(self.metro_select)

    @allure.step('Ввод номера телефона')
    def input_valid_phone_number(self, phone_number):
        self.input_text(self.number_input, phone_number)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        self.click_and_wait(self.button_next, self.about_rent_page.date_input)

    @allure.step('Клик по логотипу самоката')
    def click_samokat_logo(self):
        self.click_and_check_url_change(self.logo_samokat, 'https://qa-scooter.praktikum-services.ru/')
