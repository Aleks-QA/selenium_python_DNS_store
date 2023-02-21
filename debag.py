from random import randint

import pyautogui
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.main_page import LoginPage
from selenium.webdriver.chrome.options import Options
from base.base_class import Base
import pytest

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = 'https://www.dns-shop.ru/cart/'

driver.get(url)
driver.maximize_window()

def look_for_element(self):
    driver = self.driver
    len_element = len(driver.find_element(By.XPATH, '//p[text()="Удалить"]'))



# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="header-desktop"]/div[2]/div/div/ul/li[1]/div/div[2]/div[2]/div[1]/div/button[1]'))).click()


MEMORY_DROP_DAWN = "//div[2]/div[1]/div/div[3]/div[1]/div[8]/a"
APPLY_FILTERS = "//a[text()='Все фильтры']"


action = ActionChains(driver)


# foot = driver.find_element(By.XPATH, '//*[@id="products-list-pagination"]/button')
# action.move_to_element(foot).perform()
#
#
# def move_mouse_cursor_random():
#     pyautogui.moveTo(randint(100, 500), randint(100, 500))
#     pyautogui.moveTo(randint(100, 500), randint(100, 500))
#
# move_mouse_cursor_random()
#
# action.move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, MEMORY_DROP_DAWN)))).perform()
#
# time.sleep(1)
#
# scroll_value = -200
# scroll_by = f'window.scrollBy(0, {scroll_value});'
# driver.execute_script(scroll_by)
#
# time.sleep(1)


# def move_to_element(self, element):
#     """Переместиться к элементу"""
#     action = ActionChains(self.driver)
#     action.move_to_element(element).perform()
#     # print("Переместился к ", element)




# def move_to_elem(element):
#     """Переместиться к элементу"""
#     action = ActionChains(driver)
#     action.move_to_element(element).perform()
#     print("Переместился к ", element)
#
#
#
#
# def get_memory_drop_dawn():
#     return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, MEMORY_DROP_DAWN)))

# action.move_to_element(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, APPLY_FILTERS)))).perform()

# driver.execute_script("window.scrollTo(0, window.scrollY + 1000)")


# location_x = element.location.get('x', 0)
# location_y = element.location.get('y', 0)
# size_x = element.size.get('width', 0)
# size_y = element.size.get('height', 0)

# pyautogui.moveTo(1000, 100)
# pyautogui.moveTo(100, 200)
#
# randint(100, 500)

# pyautogui.moveRel(location_x + size_x / 2, location_y + size_y / 2)
# pyautogui.moveRel(-1, -1, 0.1)





# move_to_elem(get_memory_drop_dawn())

#
# text_p = driver.find_element(By.XPATH, '//div[3]/div/div[2]/div[1]/a').text
# print(text_p)

# x = ['6.67"', 'Смартфон', 'POCO', 'X5', '5G', '128', 'ГБ', 'голубой']
# y = '6.67" Смартфон POCO X5 5G 128 ГБ голубой'
#
# full_data = ' '.join(x)
#
# print(full_data)
# assert x == y
#


# text_p = '6.67" Смартфон POCO X5 5G 128 ГБ голубой [ядер - 8x(1.7 ГГц, 2.2 ГГц), 6 Гб, 2 SIM, AMOLED, 2400x1080, камера 48+8+2 Мп, NFC, 5G, GPS, 5000 мА*ч]'
#
#
# def slices_list(list_text, start=0, stop=0):
#     spisok = text_p.split(' ')
#     new_list = spisok[0:stop]
#     return new_list
#
#
# print(slices_list(text_p, stop=8))
# text_1 = slices_list(text_p, stop=8)
# text_2 = ['6.67"', 'Смартфон', 'POCO', 'X5', '5G', '128', 'ГБ', 'голубой']
#
# assert text_1 == text_2, 'NO'
