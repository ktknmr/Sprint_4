import pytest
from pages.main_page import MainPage
from locators import base_page_locators, main_page_locators
import allure


class TestQuestionsAboutImportant:

    @allure.parent_suite("Главная страница")
    @allure.suite("Вопросы о важном")
    @allure.sub_suite("Отображение вопросов и ответов")
    @allure.title('{question}')
    @pytest.mark.parametrize(
        'question, answer',
            zip(main_page_locators.important_questions, main_page_locators.important_answers)
    )
    def test_question_visible_and_has_answer(self, question, answer, driver):
        driver.get(base_page_locators.MAIN_PAGE_URL)
        current_question = MainPage(driver)
        current_question.find_and_show_the_question(question)
        current_question.click_on_question(question)
        current_question.make_screenshot()
        assert current_question.check_answer_is_visible(answer)


