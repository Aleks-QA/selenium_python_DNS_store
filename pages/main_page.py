import time

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class MainPage(Base):
    """Авторизация пользователя"""
    url = 'https://www.dns-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    BUTTON_ENTER_LK = '//div[@class="homepage__container"]//span[text()="Войти"]'
    BUTTON_ENTER_WITH_PASSWORD = '//div[text()="Войти с паролем"]'
    INPUT_EMAIL = '[autocomplete="username"]'
    INPUT_PASSWORD = '[autocomplete="current-password"]'
    BUTTON_AUTHORIZATION = '//div[@class="base-main-button"]//span[text()="Войти"]'
    USER_AVATAR = '[class="user-profile__level"]'
    TEXT_USER_NAME = '[class="user-profile__username"]'

    MENU_HOUSEHOLD = "//a[text()='Бытовая техника']"
    MENU_SMARTPHONES = "//a[text()='Смартфоны и фототехника']"
    HOVER_SMARTPHONES = "//span[text()='Смартфоны']"
    HOVER_TOP_CATEGORY_SMART = "//a[text()='2023 года']"

    # GETTERS

    def get_enter_lk(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.BUTTON_ENTER_LK)))

    def get_enter_with_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON_ENTER_WITH_PASSWORD)))

    def get_input_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.INPUT_EMAIL)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.INPUT_PASSWORD)))

    def get_enter_authorization(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.BUTTON_AUTHORIZATION)))


    def get_hover_top_category_smart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.HOVER_TOP_CATEGORY_SMART)))

    def get_category_smartphones(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.MENU_SMARTPHONES)))

    # ACTIONS

    def enter_lk(self):
        self.get_enter_lk().click()

    def enter_with_password(self):
        self.get_enter_with_password().click()

    def input_email(self, email):
        self.get_input_email().send_keys(email)

    def input_password(self, password):
        self.get_input_password().send_keys(password)

    def enter_authorization(self):
        self.get_enter_authorization().click()

    def click_category_smartphones(self):
        self.get_category_smartphones().click()

    def click_hover_top_category_smart(self):
        self.get_hover_top_category_smart().click()

    # METHODS

    def authorization(self):
        """Авторизация"""
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.enter_lk()
        self.enter_with_password()
        self.input_email('alexander.risk1996@gmail.com')
        self.input_password('alexander.risk1996')
        self.enter_authorization()
        # self.place_the_cursor_css(self.USER_AVATAR)
        self.assert_url(self.url)

        user_name = self.get_text_invisibility_element_css(self.TEXT_USER_NAME)
        assert user_name == 'Александр Тест', 'Wrong user!'
        print('User: ', user_name)

    def select_product_hover_menu_smart_2023_main_page(self):
        """Выбрать топ смартфонов 2023 года из hover меню"""
        self.place_the_cursor_xpath(self.MENU_HOUSEHOLD)
        time.sleep(2) # баг ДНС, при наведении на любую категорию показывает категорию бытовой техники, нужно подгрузить
        self.place_the_cursor_xpath(self.MENU_SMARTPHONES)
        print('Навели курсор на смартфоны и фототехника')
        self.place_the_cursor_xpath(self.HOVER_SMARTPHONES)
        print('Навели курсор на смартфоны')
        self.click_hover_top_category_smart()
        print('Клик на 2023 года')

    def select_product_smartphones(self):
        """Выбрать в каталоге смартфоны и фототехника"""
        self.click_category_smartphones()
        print('Выбрали категорию смартфоны и фототехника')
