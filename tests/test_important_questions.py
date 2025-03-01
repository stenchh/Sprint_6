from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.order_page import OrderPage
import allure
import pytest
class TestImportantQuestions:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        cls.main_page = MainPage(cls.driver)
        cls.order_page = OrderPage(cls.driver)

    @allure.title('Тестирование вопросов из FAQ')
    @allure.description('Проверка правильности ответов на часто задаваемые вопросы')
    @pytest.mark.parametrize("question_index, expected_answer", [
        (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
    ])
    @allure.step('Проверка ответа на вопрос')
    def test_faq_question(self, question_index, expected_answer):
        element = self.main_page.driver.find_element(*self.main_page.questions)
        self.main_page.driver.execute_script("arguments[0].scrollIntoView();", element)

        questions = self.main_page.driver.find_elements(*self.main_page.questions)
        questions[question_index].click()

        answer_locator = (By.ID, f"accordion__panel-{question_index}")
        answer_element = WebDriverWait(self.main_page.driver, 5).until(
            EC.visibility_of_element_located(answer_locator)
        )

        assert expected_answer in answer_element.text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
