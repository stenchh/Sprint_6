from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class AboutRentPage:
    date_input = [By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[1]/div/input"]
    calendar_day1 = [By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]//div[contains(@class, 'react-datepicker__day') and text()='25']"]
    calendar_day2 = [By.XPATH, "//*[@id='root'']/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[6]/div[6]"]
    lease_term_box = [By. XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]"]
    time_menu = [By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div[2]"]
    check_box_black = [By. XPATH, "//*[@id='root']/div/div[2]/div[2]/div[3]/label[1]"]
    check_box_grey = [By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[3]/label[2]"]
    order_button = [By. XPATH, "//*[@id='root']/div/div[2]/div[3]/button[2]"]
    yes_button = [By. XPATH, "//*[@id='root']/div/div[2]/div[5]/div[2]/button[2]"]

    def __init__(self, driver):
        self.driver = driver



    def input_date_through_caledar1(self):
        date_input = self.driver.find_element(*self.date_input)
        date_input.click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.calendar_day1)).click()

    def input_date_through_caledar2(self):
        date_input = self.driver.find_element(*self.date_input)
        date_input.click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.calendar_day2)).click()

    def set_the_lease_time(self):
        self.driver.find_element(*self.lease_term_box).click()
        options = self.driver.find_elements(*self.time_menu)
        options[0].click()


    def set_grey_colour(self):
        self.driver.find_element(*self.check_box_grey).click()

    def set_black_colour(self):
        self.driver.find_element(*self.check_box_black).click()

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.yes_button))

    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()