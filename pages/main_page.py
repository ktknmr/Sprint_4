from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import base_page_locators, main_page_locators
from selenium.common.exceptions import NoSuchElementException
import allure
import time

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Найти вопрос')
    def find_and_show_the_question(self, question):
        element = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, main_page_locators.question.format(question))
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Кликнуть по вопросу')
    def click_on_question(self, question):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, main_page_locators.question.format(question))
            )
        )
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, main_page_locators.question.format(question))
            )
        ).click()

    @allure.step('Проверить отображение ответа')
    def check_answer_is_visible(self, answer):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, main_page_locators.answer.format(answer))
            )
        )

    def make_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    @allure.step('Нажать кнопку "Заказать" в шапке сайта')
    def press_order_header_button(self):
        element = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, base_page_locators.order_header_button)
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element(By.XPATH, base_page_locators.order_header_button).click()
        assert self.driver.current_url == base_page_locators.ORDER_PAGE_URL

    @allure.step('Нажать кнопку "Заказать" в подвале сайта')
    def press_order_footer_button(self):
        WebDriverWait(self.driver, 3)
        element = self.driver.find_element(By.XPATH, base_page_locators.order_footer_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, base_page_locators.order_footer_button)
            )
        )
        WebDriverWait(self.driver, 3)
        self.driver.find_element(By.XPATH, base_page_locators.order_footer_button).click()
        assert self.driver.current_url == base_page_locators.ORDER_PAGE_URL

    @allure.step('Нажать на логотип "Самокат"')
    def press_scooter_logo(self):
        self.driver.find_element(By.XPATH, base_page_locators.scooter_logo_button).click()
        assert self.driver.current_url == base_page_locators.MAIN_PAGE_URL

    @allure.step('Нажать на логотип "Яндекс"')
    def press_scooter_logo(self):
        self.driver.find_element(By.XPATH, base_page_locators.scooter_logo_button).click()
        assert self.driver.current_url == base_page_locators.MAIN_PAGE_URL

    @allure.step('Перейти на новую вкладку "Яндекс"')
    def press_yandex_logo(self):
        self.driver.find_element(By.XPATH, base_page_locators.yandex_logo_button).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(EC.visibility_of_element_located((By.XPATH, base_page_locators.search_button_yandex)))
        assert self.driver.current_url == base_page_locators.YANDEX_URL
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        assert self.driver.current_url == base_page_locators.MAIN_PAGE_URL

    @allure.step('Принять куки')
    def press_accepted_cookies(self):
        flag = True
        try:
            self.driver.find_element(By.XPATH, base_page_locators.accept_cookies).click()
        except NoSuchElementException:
            flag = True
        assert flag
