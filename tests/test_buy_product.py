from selenium import webdriver
from base.base_class import Base
from conftest import set_up
from pages.cart_page import CartPage
from pages.main_page import SelectSmart2023
from pages.main_page import LoginPage
from webdriver_manager.chrome import ChromeDriverManager
from pages.checkout_finish_page import CheckoutPage
from pages.catalog_smart_2023_page import CatalogTopSmartPage
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


def test_buy_product_1(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # от лишних сообщений в терминале
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)
    base = Base(driver)

    lp = LoginPage(driver)
    lp.authorization()

    base.clean_cart()
    driver.back()

    bp = SelectSmart2023(driver)
    bp.select_product_main_page()

    top_smart_2023 = CatalogTopSmartPage(driver)
    name_and_price_catalog = top_smart_2023.add_to_cart_product_1()

    cp = CartPage(driver)
    name_and_price_cart = cp.go_to_checkout_product_1()

    assert name_and_price_catalog == name_and_price_cart, 'the name or price has changed after being added to the cart'

    checkout_p = CheckoutPage(driver)
    name_and_price_finish = checkout_p.finish_buy_product_1()

    assert name_and_price_catalog == name_and_price_finish, 'name or price changed during order confirmation'

i = 0
while i < 20:
    i += 1
    test_buy_product_1(set_up)
    print('__________________________', i)

