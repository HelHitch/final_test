import time

from selenium import webdriver
import pytest
from main_page import MainPage


# test


@pytest.fixture()
def browser():
    print('---> Open browser')
    browser = webdriver.Chrome()
    yield browser
    print('---> Close Browser')
    browser.quit()


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.parametrize('sale', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_go_to_login_page(browser, sale):
    page = MainPage(browser, sale)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    browser.maximize_window()
    login_page = page.go_to_login_page()
    login_page = page.should_be_login_link()
    add_to_basket = page.add_to_basket()
    add = page.solve_quiz_and_get_code()
    scroll = browser.execute_script("window.scrollBy(0,125);")
    time.sleep(3)
    name_check = page.assert_book_name()
    price = page.cost()

