import allure
from selenium import webdriver
from selenium.common import TimeoutException
from pages.cart_page import CartPage
from pages.main_page import MainPage
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.checkout_finish_page import CheckoutPage
from pages.smartfony_2023_goda_page import CatalogTopSmartPage
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from pages.smartfony_i_fototexnika_page import SmartfonyFototexnika


@allure.description("Test buy smartphone 2023")
def test_buy_smartphone_2023(set_up, data):
    # CHROME
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # от лишних сообщений в терминале
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

    # FIREFOX
    # option = webdriver.FirefoxOptions()
    # option.set_preference("dom.webdriver.enabled", False)  #убирает флажок что автоматизированное ПО управляет браузером
    # option.set_preference("general.useragent.override", "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    #                                                     "(KHTML, like Gecko) Chrome/51.0.2704.103"
    #                                                     " Safari/537.36")  # подмена user-agent
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=option)

    email = data['email']
    password = data['password']

    mp = MainPage(driver)
    mp.authorization(email, password)

    s_i_f = SmartfonyFototexnika(driver)
    try:
        mp.select_category_hover_menu_smart_2023_main_page()
    except TimeoutException:
        print("На сайте ДНС сейчас не работает hover меню")
        mp.click_category_smartphones()
        s_i_f.select_category_smartphones_2023()

    top_smart_2023 = CatalogTopSmartPage(driver)
    name_and_price_catalog = top_smart_2023.add_to_cart_product_1()

    cp = CartPage(driver)
    name_and_price_cart = cp.go_to_checkout_product_1()
    assert name_and_price_catalog == name_and_price_cart, 'the name or price has changed after being added to the cart'

    checkout_p = CheckoutPage(driver)
    name_and_price_finish = checkout_p.finish_buy_product_1()
    assert name_and_price_catalog == name_and_price_finish, 'name or price changed during order confirmation'

    cp.clean_cart()