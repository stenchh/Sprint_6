import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AboutRentPage(BasePage):
    date_input = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    lease_term_box = [By.CSS_SELECTOR, ".Dropdown-arrow"]
    time_menu = [By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div[2]"]
    check_box_black = [By.ID, "black"]
    check_box_grey = [By.ID, "grey"]
    order_button = [By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Middle__1CSJM')]"]
    yes_button = [By.XPATH, "//button[contains(text(), 'Да')]"]
    status_button = [By.XPATH, "//button[text()='Посмотреть статус']"]

    @allure.step('Ввод даты через календарь')
    def input_date_through_calendar(self, date):
        self.input_text(self.date_input, date)

    @allure.step('Установка времени аренды')
    def set_the_lease_time(self, index):
        self.click_element(self.lease_term_box)
        options = self.driver.find_elements(*self.time_menu)
        options[index].click()

    @allure.step('Выбор серого цвета')
    def set_grey_colour(self):
        self.click_element(self.check_box_grey)

    @allure.step('Выбор черного цвета')
    def set_black_colour(self):
        self.click_element(self.check_box_black)

    @allure.step('Клик на кнопку "Заказать"')
    def click_order_button(self):
        self.click_and_wait(self.order_button, self.yes_button)

    @allure.step('Клик на кнопку "Да"')
    def click_yes_button(self):
        self.click_and_wait(self.yes_button, self.status_button)



