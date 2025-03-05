import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(BasePage):
    upper_order_button = [By.CSS_SELECTOR, "button.Button_Button__ra12g:not(.Button_Middle__1CSJM)"]
    lower_order_button = [By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM"]
    logo = [By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/a[1]/img"]
    questions = [By.CLASS_NAME, "accordion__item"]
    answers = [By.CLASS_NAME, "accordion__panel"]

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик на верхнюю кнопку "Заказать"')
    def click_upper_order_button(self):
        self.click_and_check_url_change(self.upper_order_button, "https://qa-scooter.praktikum-services.ru/order")

    @allure.step('Клик на нижнюю кнопку "Заказать"')
    def click_lower_order_button(self):
        self.scroll_and_click(self.lower_order_button)  # Если у вас есть scroll_and_click, используем его
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://qa-scooter.praktikum-services.ru/order"))

    @allure.step('Переход на сайт Дзена')
    def click_on_logo(self):
        self.click_element(self.logo)

        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        self.wait.until(EC.url_to_be("https://dzen.ru/?yredirect=true"))
        return self.driver.current_url

    @allure.step('Клик по вопросу в FAQ')
    def click_question(self, index):
        self.find_and_click(self.questions, index)

    @allure.step('Получение текста ответа на вопрос')
    def get_answer_text(self, index):
        answer_locator = (By.ID, f"accordion__panel-{index}")
        return self.get_element_text(answer_locator)
