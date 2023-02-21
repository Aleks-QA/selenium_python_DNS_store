from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class LoginPage(Base):
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

    # GETTERS

    def get_enter_lk(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.BUTTON_ENTER_LK)))

    def get_enter_with_password(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON_ENTER_WITH_PASSWORD)))

    def get_input_email(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.INPUT_EMAIL)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.INPUT_PASSWORD)))

    def get_enter_authorization(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.BUTTON_AUTHORIZATION)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.TEXT_USER_NAME)))

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

    def text_user_name(self):
        user_name = self.get_user_name().text
        return user_name

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
        self.place_the_cursor_css(self.USER_AVATAR)
        self.assert_url(self.url)
        user_name_test = self.text_user_name()
        print('User: ', user_name_test)
        assert user_name_test == 'Александр Тест', 'Wrong user!'


class SelectSmart2023(Base):
    """Выбрать категорию: смартфоны 2023"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    MENU_SMARTPHONES = "//a[text()='Смартфоны и фототехника']"
    HOVER_SMARTPHONES = "//div[2]/div[1]/div[1]/a[1]"
    HOVER_TOP_CATEGORY_SMART = '//span[@class="header-menu-desktop__popup"]/a[1]'

    # GETTERS

    def get_hover_top_category_smart(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.HOVER_TOP_CATEGORY_SMART)))

    # ACTIONS

    def click_hover_top_category_smart(self):
        self.get_hover_top_category_smart().click()

    # METHODS

    def select_product_main_page(self):
        """Выбрать топ смартфонов 2023 года из hover меню"""
        self.place_the_cursor_xpath(self.MENU_SMARTPHONES)
        self.place_the_cursor_xpath(self.HOVER_SMARTPHONES)
        self.click_hover_top_category_smart()
