from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class CatalogTopSmartPage(Base):
    """Каталог топ смартфонов 2023 года"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    NAME_PRODUCT_1 = '//div[3]/div/div[2]/div[1]/a'  # //div[3]/div/div[2]/div[number]/a
    PRICE_PRODUCT_1 = '//div/div[2]/div[1]/div[4]/div/div[1]'  # //div/div[2]/div[number]/div[4]/div/div[1]
    BUY_OR_ADD_CART_PRODUCT_1 = '//div/div[2]/div[1]/div[4]/button[2]'  # //div/div[2]/div[number]/div[4]/button[2]
    CART_BUTTON = 'a[class="buttons__link ui-link cart-link-counter"]'
    CHECKBOX_RATING_4 = '//div[2]/div[1]/div/div[3]/div[1]/div[2]/label'
    INPUT_MIN_PRICE = '//div[3]/div[1]/div[4]/div/div/div[1]/input'
    INPUT_MAX_PRICE = 'div.left-filters__list > div:nth-child(4) > div > div > div:nth-child(2) > input'
    MEMORY_DROP_DAWN = "//div[2]/div[1]/div/div[3]/div[1]/div[8]/a"
    MEMORY_CHECKBOX_128 = '//div[1]/div/div[3]/div[1]/div[8]/div/div/div[2]/label[1]'
    RAM_DROP_DAWN = "//span[text()='Объем оперативной памяти']"
    RAM_CHECKBOX_8 = '//div[1]/div[10]/div/div/div[2]/label[2]'
    WEIGHT_DROP_DAWN = "//span[text()='Вес (г)']"
    WEIGHT_CHECK_BOX_159 = "//div[17]/div[3]/div[1]/div[1]/div/div[3]/label[3]/span"
    APPLY_FILTERS = "//div[@class='filters-extended__buttons']/button[text()='Применить']"
    ALL_FILTERS = "//a[text()='Все фильтры']"

    # GETTERS

    def get_checkbox_rating_4(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.CHECKBOX_RATING_4)))

    def get_input_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.INPUT_MIN_PRICE)))

    def get_input_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.INPUT_MAX_PRICE)))

    def get_memory_drop_dawn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.MEMORY_DROP_DAWN)))

    def get_memory_checkbox_128(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.MEMORY_CHECKBOX_128)))

    def get_ram_drop_dawn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.RAM_DROP_DAWN)))

    def get_ram_checkbox_8(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.RAM_CHECKBOX_8)))

    def get_all_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ALL_FILTERS)))

    def get_weight_drop_dawn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.WEIGHT_DROP_DAWN)))

    def get_weight_checkbox_159(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.WEIGHT_CHECK_BOX_159)))

    def get_apply_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.APPLY_FILTERS)))

    def get_name_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.NAME_PRODUCT_1)))

    def get_price_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.PRICE_PRODUCT_1)))

    def get_add_to_cart_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.BUY_OR_ADD_CART_PRODUCT_1)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.CART_BUTTON)))

    # ACTIONS

    def apply_filters(self):
        self.move_to_element(self.get_apply_filters())
        self.get_apply_filters().click()

    def checkbox_rating_4(self):
        self.move_to_element(self.get_checkbox_rating_4())
        self.get_checkbox_rating_4().click()

    def input_min_price(self):
        self.move_to_element(self.get_input_min_price())
        self.get_input_min_price().send_keys('10000')

    def input_max_price(self):
        self.get_input_max_price().send_keys('100000')

    def memory_drop_dawn(self):
        self.move_to_element(self.get_memory_drop_dawn())
        self.get_memory_drop_dawn().click()

    def memory_checkbox_128(self):
        self.move_to_element(self.get_memory_checkbox_128())
        self.get_memory_checkbox_128().click()

    def ram_drop_dawn(self):
        self.move_to_element(self.get_ram_drop_dawn())
        self.get_ram_drop_dawn().click()

    def ram_checkbox_8(self):
        self.move_to_element(self.get_ram_checkbox_8())
        self.get_ram_checkbox_8().click()

    def all_filter(self):
        self.move_to_element(self.get_all_filter())
        self.get_all_filter().click()

    def weight_drop_dawn(self):
        self.move_to_element(self.get_weight_drop_dawn())
        self.get_weight_drop_dawn().click()

    def weight_checkbox_159(self):
        self.move_to_element(self.get_weight_checkbox_159())
        self.get_weight_checkbox_159().click()

    def click_add_to_cart_product_1(self):
        self.move_to_element(self.get_add_to_cart_product_1())
        self.get_add_to_cart_product_1().click()

    def click_cart_button(self):
        self.move_to_element(self.get_cart_button())
        self.get_cart_button().click()

    def text_name_product_1(self):
        return self.get_name_product_1().text

    def text_price_product_1(self):
        return self.get_price_product_1().text

    # METHODS

    def add_to_cart_product_1(self):
        """Выбрать фильтры, сохранить название и цену товара, добавить и перейти в корзину"""
        self.move_to_element(self.get_all_filter())
        self.checkbox_rating_4()
        print('Выбран фильтр: рейтинг 4 и выше ')
        self.input_min_price()
        print('Выбран фильтр: минимальная цена ')
        self.input_max_price()
        print('Выбран фильтр: максимальная цена ')
        self.memory_drop_dawn()
        self.memory_checkbox_128()
        print('Выбран фильтр: объем встроенной памяти ')
        self.ram_drop_dawn()
        self.ram_checkbox_8()
        print('Выбран фильтр: объем оперативной памяти ')
        self.all_filter()
        self.weight_drop_dawn()
        self.weight_checkbox_159()
        print('Выбран фильтр: вес устройства ')
        self.apply_filters()
        print('Фильтры применены ')
        self.click_add_to_cart_product_1()

        text_name = self.slices_list(list_text=self.text_name_product_1(), stop=8)
        text_price = self.slices_list(list_text=self.text_price_product_1(), stop=2)

        self.click_cart_button()
        print(f"Название товара в каталоге: {text_name}, его стоимость: {text_price}")
        return text_name, text_price
