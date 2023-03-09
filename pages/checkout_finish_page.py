from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger
import allure


class CheckoutPage(Base):
    """Корзина товаров"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    DROP_DAWN_PRODUCT = '//*[@id="checkout"]/div/div[1]/div[1]/div/div/div[2]/div'
    # DROP_DAWN_PRODUCT = '//*[@id="checkout"]/div/div[1]/div/div/div[2]'
    NAME_PRODUCT_1_FINISH = '//div/div/div[3]/div/div/div[@class="base-checkout-products-list__item-title_xXL"]'
    # NAME_PRODUCT_1_FINISH = '//*[@id="checkout"]/div/div[1]//div[3]/div/div[1]/div[1]'
    PRICE_PRODUCT_FINISH = '//*[@id="checkout"]/div/div[1]//div[1]/div[2]/div[1]'

    # GETTERS

    def get_drop_dawn_finish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.DROP_DAWN_PRODUCT)))

    def get_name_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.NAME_PRODUCT_1_FINISH)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.PRICE_PRODUCT_FINISH)))

    # ACTIONS

    def click_drop_dawn_finish(self):
        self.get_drop_dawn_finish().click()

    def text_name_product_1(self):
        return self.get_name_product_1().text

    def text_price_product(self):
        return self.get_price_product().text

    # METHODS

    def finish_buy_product_1(self):
        """Проверить название и цену товара во время оформления заказа, сделать скриншот"""
        with allure.step('Finish buy product 1'):
            Logger.add_start_step(method='finish_buy_product_1')
            self.get_current_url()
            text_price_finish = self.slices_list(list_text=self.text_price_product(), start=1, stop=3)
            self.click_drop_dawn_finish()
            text_name_finish = self.slices_list(list_text=self.text_name_product_1(), stop=8)
            print(f"Название товара во время подтверждения заказа: {text_name_finish}, его стоимость: {text_price_finish}")
            self.get_screenshot()
            Logger.add_end_step(self.driver.current_url, method='finish_buy_product_1')
            return text_name_finish, text_price_finish
