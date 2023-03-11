import pytest
from pages.main_page import MainPage
from locators import base_page_locators, main_page_locators
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import allure


class TestQuestionsAboutImportant:

    driver = None

    @classmethod
    def setup_class(cls):
        firefox_options = Options()
        firefox_options.add_argument('-headless')
        cls.driver = webdriver.Firefox(options=firefox_options)

    @allure.parent_suite("Главная страница")
    @allure.suite("Вопросы о важном")
    @allure.sub_suite("Отображение вопросов и ответов")
    @allure.title('{question}')
    @pytest.mark.parametrize(
        'question, answer',
            zip(main_page_locators.important_questions, main_page_locators.important_answers)
    )
    def test_question_visible_and_has_answer(self, question, answer):
        self.driver.get(base_page_locators.MAIN_PAGE_URL)
        current_question = MainPage(self.driver)
        current_question.find_and_show_the_question(question)
        current_question.click_on_question(question)
        current_question.make_screenshot()
        assert current_question.check_answer_is_visible(answer)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

