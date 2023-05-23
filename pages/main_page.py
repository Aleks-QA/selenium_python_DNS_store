import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):
    """Главная страница"""
    url = 'https://www.dns-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    BUTTON_LOCATION_OK_FOOTER = '//div/*[@class="bottom-sheet__footer"]//span[contains(text(), "Всё верно")]'
    BUTTON_LOCATION_OK = '//span[contains(text(), "Всё верно")]'
    # BUTTON_ENTER_LK = '//div[@class="homepage__container"]//span[text()="Войти"]'
    LOGIN_ICON_LK = '//div[text()="Войти"]'
    BUTTON_ENTER_LK = '//span[text()="Войти"]'
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

    def get_button_location_ok(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.BUTTON_LOCATION_OK)))

    def get_icon_lk(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.LOGIN_ICON_LK)))

    def get_button_lk(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.BUTTON_ENTER_LK)))

    def get_enter_with_password(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON_ENTER_WITH_PASSWORD)))

    def get_input_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.INPUT_EMAIL)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.INPUT_PASSWORD)))

    def get_enter_authorization(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.BUTTON_AUTHORIZATION)))

    def get_hover_top_category_smart(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.HOVER_TOP_CATEGORY_SMART)))

    def get_category_smartphones(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.MENU_SMARTPHONES)))

    # ACTIONS

    def click_button_location_ok(self):
        self.get_button_location_ok().click()

    def enter_lk(self):
        self.get_icon_lk().click()

    def click_lk(self):
        self.get_button_lk().click()

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

    def authorization(self, email, password):
        """Авторизация пользователя"""
        with allure.step('Authorization'):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            time.sleep(0.5)
            self.get_current_url()
            self.click_button_location_ok()
            self.place_the_cursor_xpath(self.LOGIN_ICON_LK)
            # self.enter_lk()
            self.click_lk()
            self.enter_with_password()
            self.input_email(email)
            self.input_password(password)
            time.sleep(2)
            self.enter_authorization()
            self.assert_url(self.url)
            user_name = self.get_text_invisibility_element_css(self.TEXT_USER_NAME)
            assert user_name == 'Александр Тест', 'Wrong user!'
            print('User: ', user_name)
            Logger.add_end_step(url=self.driver.current_url, method='authorization')

    def select_category_hover_menu_smart_2023_main_page(self):
        """Выбрать топ смартфонов 2023 года из hover меню"""
        with allure.step('Select category hover menu smartphone 2023 main page'):
            Logger.add_start_step(method='select_product_hover_menu_smart_2023_main_page')
            self.get_current_url()
            self.place_the_cursor_xpath(self.MENU_HOUSEHOLD)
            time.sleep(3)
            self.place_the_cursor_xpath(self.MENU_SMARTPHONES)
            print('Навели курсор на смартфоны и фототехника')
            self.place_the_cursor_xpath(self.HOVER_SMARTPHONES)
            print('Навели курсор на смартфоны')
            self.click_hover_top_category_smart()
            print('Клик на 2023 года')
            Logger.add_end_step(self.driver.current_url, method='select_category_hover_menu_smart_2023_main_page')
