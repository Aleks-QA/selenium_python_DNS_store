from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class CartPage(Base):
    """Корзина товаров"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    NAME_PRODUCT_1 = '//*[@id="cart-page-new"]/div[1]/div[2]//div[1]/div[3]/div/div[1]/a'  # //div[numder]/div/div[1]/div[1]/div[1]/div[3]/div/div[1]/a
    PRICE_PRODUCT_1 = '//div/div/div/div[1]/div[1]/div[3]/div/div[1]/div[1]/span[2]'  # //div/div[number]/div/div[1]/div[1]/div[3]/div/div[1]/div[1]/span[2]]
    GO_TO_CHECKOUT = '//span[text()="Перейти к оформлению"]'

    # GETTERS

    def get_name_product_1(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.NAME_PRODUCT_1)))

    def get_price_product_1(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.PRICE_PRODUCT_1)))

    def get_go_to_checkout(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.GO_TO_CHECKOUT)))

    # ACTIONS

    def click_go_to_checkout(self):
        self.get_go_to_checkout().click()

    def text_cart_name_product_1(self):
        return self.get_name_product_1().text

    def text_cart_price_product_1(self):
        return self.get_price_product_1().text

    # METHODS

    def go_to_checkout_product_1(self):
        """Проверить название и цену товара и перейти к оформлению"""
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
        return text_name_product_1, text_price_product_1
