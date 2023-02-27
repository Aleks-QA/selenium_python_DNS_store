import time
import datetime
import pyautogui
from random import randint
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver):
        self.driver = driver

    def place_the_cursor_css(self, selector_css):
        """Навести курсор на элемент CSS"""
        hoverable = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector_css)))
        ActionChains(self.driver).move_to_element(hoverable).perform()

    def place_the_cursor_xpath(self, selector_xpath):
        """Навести курсор на элемент XPATH"""
        hoverable = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, selector_xpath)))
        ActionChains(self.driver).move_to_element(hoverable).perform()

    def move_to_element(self, element):
        """Переместиться к элементу + скролл"""
        scroll_by = 'window.scrollBy(0, -200);'
        self.driver.execute_script(scroll_by)

        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def move_mouse_cursor_random(self):
        """Перемещение курсора на рандомное расстояние, если этого требует сайт"""
        pyautogui.moveTo(randint(100, 500), randint(100, 500))
        pyautogui.moveTo(randint(100, 500), randint(100, 500))

    def get_text_invisibility_element_css(self, locator_css):
        """Получаем текст из невидимого элемента"""
        time.sleep(3)
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_css)))
        text = self.driver.execute_script("return arguments[0].innerHTML", element)
        print("Text element: ", text)
        return text

    def assert_word(self, word, result):
        """Проверяем текст"""
        value_word = word.text
        assert value_word == result, 'Текст не совпадает с заданным'
        print('Good value word')

    def slices_list(self, list_text, start=0, stop=0):
        """Получить срез текста и вернуть строку"""
        list_slice = list_text.split(' ')
        new_list = list_slice[start:stop]
        full_data = ' '.join(new_list)
        return full_data

    def get_current_url(self):
        """Метод возвращающий URL"""
        get_url = self.driver.current_url
        print(f'Current URL: {get_url}')
        return get_url

    def assert_url(self, result):
        """Проверяем URL с заданным"""
        get_url = self.driver.current_url
        assert get_url == result, 'Адрес не совпадает с заданным'
        print('Good value URL')

    def get_screenshot(self):
        """Создание скриншотов"""
        now_date = (datetime.datetime.utcnow() + datetime.timedelta(hours=+3)).strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot(
            '.\\screen\\' + name_screenshot)
        print('Сделан скриншот')
