import allure
from selenium import webdriver
from pages.cart_page import CartPage
from pages.main_page import MainPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


@allure.description("Test clean cart")
def test_clean_cart(set_up, data):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # от лишних сообщений в терминале
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

    email = data['email']
    password = data['password']

    mp = MainPage(driver)
    mp.authorization(email, password)

    cp = CartPage(driver)
    cp.clean_cart()