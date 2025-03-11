import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    upper_order_button = [By.CSS_SELECTOR, "button.Button_Button__ra12g"]
    lower_order_button = [By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM"]
    logo = [By.CSS_SELECTOR, "img[src='/assets/ya.svg']"]
    questions = [By.CLASS_NAME, "accordion__item"]
    answers = [By.CLASS_NAME, "accordion__panel"]

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик на верхнюю кнопку "Заказать"')
    def click_upper_order_button(self):
        self.click_element(self.upper_order_button)
        return self.get_current_url()

    @allure.step('Клик на нижнюю кнопку "Заказать"')
    def click_lower_order_button(self):
        self.scroll_and_click(self.lower_order_button)
        return self.get_current_url()

    @allure.step('Переход на сайт Дзена')
    def click_on_logo(self):
        self.click_element(self.logo)
        self.switch_to_new_tab()
        self.wait_for_url("https://dzen.ru/?yredirect=true")
        return self.get_current_url()

    @allure.step('Клик по вопросу в FAQ')
    def click_question(self, index):
        self.find_and_click(self.questions, index)

    @allure.step('Получение текста ответа на вопрос')
    def get_answer_text(self, index):
        answer_locator = (By.ID, f"accordion__panel-{index}")
        return self.get_element_text(answer_locator)
