import pytest
import allure
from pages.main_page import MainPage
from selenium import webdriver
from data import FAQ_DATA

class TestImportantQuestions:
    @allure.title('Тестирование вопросов из FAQ')
    @allure.description('Проверка правильности ответов на часто задаваемые вопросы')
    @pytest.mark.parametrize("question_index, expected_answer", FAQ_DATA)
    def test_faq_questions(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)

        main_page.click_question(question_index)
        actual_answer = main_page.get_answer_text(question_index)
        assert expected_answer in actual_answer

