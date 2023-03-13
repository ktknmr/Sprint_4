from pages.order_page import OrderPage
from locators import base_page_locators
import allure
from data_for_test import testing_data
import pytest


class TestMakeOrder:

    @allure.parent_suite('Оформление заказа')
    @allure.suite('Через кнопку "Заказать" в шапке')
    @allure.sub_suite("Позитивные сценарии")
    @allure.title('Позитивный сценарий')
    @pytest.mark.parametrize('data', testing_data)
    def test_make_order_from_header_button(self, data, driver):
        driver.get(base_page_locators.MAIN_PAGE_URL)
        order = OrderPage(driver)
        order.press_accepted_cookies()
        order.press_order_header_button()
        order.create_successful_order(data)
        order.press_scooter_logo()
        order.press_yandex_logo()

    @allure.parent_suite('Оформление заказа')
    @allure.suite('Через кнопку "Заказать" в футере')
    @allure.sub_suite("Позитивные сценарии")
    @allure.title('Позитивный сценарий')
    @pytest.mark.parametrize('data', testing_data)
    def test_make_order_from_footer_button(self, data, driver):
        driver.get(base_page_locators.MAIN_PAGE_URL)
        order = OrderPage(driver)
        order.press_accepted_cookies()
        order.press_order_footer_button()
        order.create_successful_order(data)
        order.press_scooter_logo()
        order.press_yandex_logo()
