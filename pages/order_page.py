from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import order_page_locators, base_page_locators
from pages.main_page import MainPage
import allure


class OrderPage(MainPage):

    @allure.step('Заполнить поле "Имя"')
    def set_name(self, name):
        self.driver.find_element(By.XPATH, order_page_locators.name).send_keys(name)

    @allure.step('Заполнить поле "Фамилия"')
    def set_surname(self, surname):
        self.driver.find_element(By.XPATH, order_page_locators.surname).send_keys(surname)

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        self.driver.find_element(By.XPATH, order_page_locators.address).send_keys(address)

    @allure.step('Заполнить поле "Станция метро"')
    def set_station(self, station):
        self.driver.find_element(By.XPATH, order_page_locators.station_list).click()
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, order_page_locators.station.format(station))
            )
        )
        self.driver.find_element(By.XPATH, order_page_locators.station.format(station)).click()

    @allure.step('Заполнить поле "Телефон"')
    def set_phone_number(self, phone_number):
        self.driver.find_element(By.XPATH, order_page_locators.phone_number).send_keys(phone_number)

    @allure.step('Заполнение страницы "Для кого самокат"')
    def fill_order_data(self, data):
        self.set_name(data['name'])
        self.set_surname(data['surname'])
        self.set_address(data['address'])
        self.set_station(data['station'])
        self.set_phone_number(data['phone_number'])

    @allure.step('Заполнить поле "Когда привезти самокат"')
    def set_delivery_date(self, delivery_date):
        self.driver.find_element(By.XPATH, order_page_locators.delivery_date_field).click()
        self.driver.find_element(By.XPATH, order_page_locators.delivery_day.format(delivery_date)).click()

    @allure.step('Заполнить поле "Срок аренды"')
    def set_rent_duration(self, rent_duration):
        self.driver.find_element(By.XPATH, order_page_locators.rent_duration_list).click()
        self.driver.find_element(By.XPATH, order_page_locators.rent_duration.format(rent_duration)).click()

    @allure.step('Заполнить поле "Цвет самоката"')
    def set_scooter_color(self, scooter_color):
        self.driver.find_element(By.XPATH, order_page_locators.scooter_color.format(scooter_color)).click()

    @allure.step('Заполнить поле "Комментарий для курьера"')
    def set_comment_for_the_courier(self, comment_for_the_courier):
        self.driver.find_element(By.XPATH, order_page_locators.comment_for_the_courier).send_keys(comment_for_the_courier)

    @allure.step('Заполнение страницы "Про аренду"')
    def fill_delivery_data(self, data):
        self.set_delivery_date(data['delivery_date'])
        self.set_rent_duration(data['rent_duration'])
        self.set_scooter_color(data['scooter_color'])
        self.set_comment_for_the_courier(data['comment_for_the_courier'])

    @allure.step('Нажать кнопку "Далее"')
    def press_continue_button(self):
        self.driver.find_element(By.XPATH, order_page_locators.continue_button).click()

    @allure.step('Нажать кнопку "Заказать"')
    def press_order_button(self):
        self.driver.find_element(By.XPATH, order_page_locators.order_button).click()

    @allure.step('Нажать кнопку "Да"')
    def press_confirm_button(self):
        self.driver.find_element(By.XPATH, order_page_locators.confirm_button).click()


    @allure.step('Нажать кнопку "Посмотреть статус"')
    def press_check_status_button(self):
        self.driver.find_element(By.XPATH, order_page_locators.check_status_button).click()
        assert  self.driver.current_url.startswith(base_page_locators.TRACK_URL)

    @allure.step('Оформление успешного заказа')
    def create_successful_order(self, data):
        self.fill_order_data(data)
        self.press_continue_button()
        self.fill_delivery_data(data)
        self.press_order_button()
        self.press_confirm_button()
        self.make_screenshot()
        self.press_check_status_button()

