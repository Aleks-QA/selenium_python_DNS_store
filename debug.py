from random import randint

import pyautogui
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from selenium.webdriver.chrome.options import Options
from base.base_class import Base
import pytest

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# url = 'https://www.dns-shop.ru/'

# base = Base(driver)
# driver.get(url)
# driver.maximize_window()








# input_text = '6.67" Смартфон POCO X5 5G 128 ГБ голубой [ядер - 8x(1.7 ГГц, 2.2 ГГц), 6 Гб, 2 SIM, AMOLED, 2400x1080, камера 48+8+2 Мп, NFC, 5G, GPS, 5000 мА*ч]'
# input_2_text = 'X5 5G 128 ГБ голубой'
#
# def find_substring(substring, string):
#     """Поиск подстроки в строке"""
#     if substring in string:
#         rez = 0
#         print("Входит!")
#     else:
#         rez = -1
#         print('Не входит')
#     assert rez == 0, 'substring not found'
#
#
#
# find_substring(input_2_text, input_text)


# from re import search
# fullstring = "pythonist"
# substring = "python"
# if search(substring, fullstring):
#     print "Подстрока найдена!"
# else:
#     print "Подстрока не найдена!"


#
#
# list_x = list(input)
# good_data = ["a", "d", 'c', 'b']
# list_index = []
# min_list_index = 0
#
#
# def find_index(min_index):
#     global min_list_index
#     i = 0
#     while i < len(good_data):
#         s = ''.join(list_x[min_index:])
#         index = s.find(good_data[i])
#         list_index.append(index)
#         min_index = min(list_index) + 1
#         if index == -1:
#             min_list_index = 10
#             break
#         i += 1
#     return list_index, min_list_index
#
#
# i = 0
# count = 0
# min_index = 0
#
# while count < len(list_x):
#     list_index, min_list_index = find_index(min_index)
#     if min_list_index == 10:
#         break
#     count += 1
#
# length = max(list_index) - min(list_index)
# print(length)





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
