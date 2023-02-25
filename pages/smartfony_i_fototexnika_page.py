from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
from utilities.logger import Logger


class SmartfonyFototexnika(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    CATEGORY_SMART_2023 = "//a[text()='2023 года']"

    # GETTERS

    def get_category_smart_2023(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.CATEGORY_SMART_2023)))

    # ACTIONS

    def click_category_smart_2023(self):
        self.get_category_smart_2023().click()

    # METHODS

    def select_category_smartphones_2023(self):
        """Выбрать категорию смартфоны 2023 года"""
        with allure.step('Select category smartphones'):
            Logger.add_start_step('select_category_smartphones')
            self.get_current_url()
            self.click_category_smart_2023()
            print('Выбрали категорию смартфоны 2023 года')
            Logger.add_end_step(self.driver.current_url, method='select_category_smartphones')
