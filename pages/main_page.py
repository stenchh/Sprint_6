from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.order_page import OrderPage


class MainPage:
    upper_order_button = [By. XPATH, "//*[@id='root']/div/div/div[1]/div[2]/button[1]"]
    lower_order_button = [By. XPATH, "//*[@id='root']/div/div/div[4]/div[2]/div[5]/button"]
    logo = [By. XPATH, "//*[@id='root']/div/div/div[1]/div[1]/a[1]/img"]
    questions = [By.CLASS_NAME, "accordion__item"]
    answers = [By.CLASS_NAME, "accordion__panel"]




    def __init__(self, driver):
        self.driver = driver
        self.order_page = OrderPage(driver)

    def click_upper_order_button(self):
        self.driver.find_element(*self.upper_order_button).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/order"))

    def click_lower_order_button(self):
        element = self.driver.find_element(*self.lower_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/order"))

    def click_on_logo(self):
        self.driver.find_element(*self.logo).click()
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be("https://dzen.ru/?yredirect=true"))


    def click_on_questions_and_check_answers(self, expected_answers):
        questions = self.driver.find_elements(*self.questions)

        for index, question in enumerate(questions):
            self.driver.execute_script("arguments[0].scrollIntoView();", question)  # Скроллим к вопросу
            question.click()
            answer_locator = (By.ID, f"accordion__panel-{index}")
            answer_element = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(answer_locator))
            assert expected_answers[index] in answer_element.text




