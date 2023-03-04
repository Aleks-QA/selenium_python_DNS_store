from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger
import allure


class CartPage(Base):
    """Корзина товаров"""
    url = 'https://www.dns-shop.ru/cart/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    NAME_PRODUCT_1 = '//*[@id="cart-page-new"]/div[1]/div[2]//div[1]/div[3]/div/div[1]/a'  # //div[numder]/div/div[1]/div[1]/div[1]/div[3]/div/div[1]/a
    TOTAL_PRICE = '//div[@class="summary-header__sum"]//span[@class="price__current"]'  # //div/div[number]/div/div[1]/div[1]/div[3]/div/div[1]/div[1]/span[2]]
    GO_TO_CHECKOUT = '//span[text()="Перейти к оформлению"]'
    DELITE_PRODUCT = '//p[text()="Удалить"]'
    DELITE_ALL = '//div[text()="Удалить выбранные"]'
    TEXT_CART_EMPTY = '.empty-message__title-empty-cart'

    # GETTERS

    def get_name_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.NAME_PRODUCT_1)))

    def get_price_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.TOTAL_PRICE)))

    def get_go_to_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.GO_TO_CHECKOUT)))

    def get_delite_product(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, self.DELITE_PRODUCT)))

    def get_delite_all_product(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, self.DELITE_ALL)))

    def get_text_cart_empty(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.TEXT_CART_EMPTY)))

    # ACTIONS

    def click_go_to_checkout(self):
        self.get_go_to_checkout().click()

    def text_cart_name_product_1(self):
        return self.get_name_product_1().text

    def text_cart_price_product_1(self):
        return self.get_price_product_1().text

    def click_delite_product(self):
        self.get_delite_product().click()

    def click_delite_all_product(self):
        self.get_delite_all_product().click()

    def text_cart_empty(self):
        return self.get_text_cart_empty().text

    # METHODS

    def go_to_checkout_product_1(self):
        """Проверить название и цену товара и перейти к оформлению"""
        with allure.step('Go to checkout product 1'):
            Logger.add_start_step(method='go_to_checkout_product_1')
            self.get_current_url()
            try:
                text_name_product_1 = self.get_name_product_1().text
                text_price_product_1 = self.slices_list(list_text=self.text_cart_price_product_1(), stop=2)
                print(f"Название товара в корзине: {text_name_product_1}, его стоимость: {text_price_product_1}")
            except TimeoutException:
                self.driver.refresh()
                text_name_product_1 = self.get_name_product_1().text
                text_price_product_1 = self.slices_list(list_text=self.text_cart_price_product_1(), stop=2)
                print(f"Название товара в корзине: {text_name_product_1}, его стоимость: {text_price_product_1}")
            self.click_go_to_checkout()
            Logger.add_end_step(self.driver.current_url, method='go_to_checkout_product_1')
            return text_name_product_1, text_price_product_1

    def clean_cart(self):
        """Удалить товар/товары из корзины"""
        with allure.step('Clean cart'):
            Logger.add_start_step(method='clean_cart')
            print('Очистка корзины')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            try:
                try:
                    self.click_delite_all_product()
                    clean_text = self.text_cart_empty()
                    assert clean_text == 'Корзина пуста', 'cart is not empty'
                    print("Товары были удалены из корзины")
                except TimeoutException:
                    self.click_delite_product()
                    clean_text = self.text_cart_empty()
                    assert clean_text == 'Корзина пуста', 'cart is not empty'
                    print("Товар удален из корзины")
            except TimeoutException:
                clean_text = self.text_cart_empty()
                assert clean_text == 'Корзина пуста', 'cart is not empty'
                print("Корзина была пуста")
            Logger.add_end_step(self.driver.current_url, method='clean_cart')
