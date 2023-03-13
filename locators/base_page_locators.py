# urls
MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'
ORDER_PAGE_URL = MAIN_PAGE_URL + 'order'
TRACK_URL = MAIN_PAGE_URL + 'track?t='
YANDEX_URL = 'https://dzen.ru/?yredirect=true'
# logo button locator
scooter_logo_button = './/a[@class="Header_LogoScooter__3lsAR"]'
# yandex button locator
yandex_logo_button = './/a[@href="//yandex.ru"]'
# button on yandex page locator
search_button_yandex = './/span[@aria-label="Логотип Дзен"]'
# order-button header locator
order_header_button = './/div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]'
# order-button footer locator
order_footer_button = './/div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]'
# accept cookies
accept_cookies = './/button[text()="да все привыкли"]'