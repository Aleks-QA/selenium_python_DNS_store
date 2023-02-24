from selenium import webdriver
from selenium.common import TimeoutException
from base.base_class import Base
from pages.cart_page import CartPage
from pages.main_page import MainPage
from webdriver_manager.chrome import ChromeDriverManager
from pages.checkout_finish_page import CheckoutPage
from pages.smartfony_2023_goda_page import CatalogTopSmartPage
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from pages.smartfony_i_fototexnika_page import SmartfonyFototexnika


def test_buy_smartphone_2023(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # от лишних сообщений в терминале
    # options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

    base = Base(driver)
    mp = MainPage(driver)

    email = 'alexander.risk1996@gmail.com'
    password = 'alexander.risk1996'
    mp.authorization(email, password)

    s_i_f = SmartfonyFototexnika(driver)
    try:
        mp.select_product_hover_menu_smart_2023_main_page()
    except TimeoutException:
        print("На сайте ДНС сейчас не работает hover меню")
        mp.click_category_smartphones()
        s_i_f.select_product_smartphones()

    top_smart_2023 = CatalogTopSmartPage(driver)
    name_and_price_catalog = top_smart_2023.add_to_cart_product_1()

    cp = CartPage(driver)
    name_and_price_cart = cp.go_to_checkout_product_1()

    assert name_and_price_catalog == name_and_price_cart, 'the name or price has changed after being added to the cart'

    checkout_p = CheckoutPage(driver)
    name_and_price_finish = checkout_p.finish_buy_product_1()

    base.clean_cart()

    assert name_and_price_catalog == name_and_price_finish, 'name or price changed during order confirmation'

# i = 1
# while i < 5:
#     i += 1
#     test_buy_product_1()
#     print('__________________________', i)

