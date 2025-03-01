from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.about_rent_page import AboutRentPage
import pytest

class OrderPage:
    name_input = [By. XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/input"]
    surname_input = [By. XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/input"]
    address_input = [By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[3]/input"]
    number_input = [By. XPATH, "//*[@id='root']/div/div[2]/div[2]/div[5]/input"]
    button_next = [By.XPATH, "//*[@id='root']/div/div[2]/div[3]/button"]
    logo_samokat = [By. XPATH, "//*[@id='root']/div/div[1]/div[1]/a[2]/img"]
    metro_input = [By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[4]/div/div/input"]
    metro_select = [By.XPATH, "//*[@class='select-search__select']"]


    def __init__(self,driver):
        self.driver = driver
        self.about_rent_page = AboutRentPage(driver)


    def input_valid_name(self, generate_name_or_surname):
        name = generate_name_or_surname
        self.driver.find_element(*self.name_input).send_keys(name)

    def input_valid_surname(self, generate_name_or_surname):
        surname = generate_name_or_surname
        self.driver.find_element(*self.surname_input).send_keys(surname)

    def input_valid_address(self,generate_address):
        address = generate_address
        self.driver.find_element(*self.address_input).send_keys(address)

    def input_metro_station(self):
        self.driver.find_element(*self.metro_input).send_keys('Полянка')
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_all_elements_located(self.metro_select))
        self.driver.find_element(*self.metro_select).click()

    def input_valid_phone_number(self,generate_phone_number):
        phone_number = generate_phone_number
        self.driver.find_element(*self.number_input).send_keys(phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.button_next).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(tuple(self.about_rent_page.date_input)))


    def click_samokat_logo(self):
        self.driver.find_element(*self.logo_samokat).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be('https://qa-scooter.praktikum-services.ru/'))


