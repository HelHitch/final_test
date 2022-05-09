from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

from base_page import BasePage
from locators import MainPageLocators
from selenium.webdriver.common.by import By
from login_page import LoginPage
import math


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        #login_link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def add_to_basket(self):
        backet_btn = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET)
        backet_btn.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"\nYour code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def assert_book_name(self):
        n = self.browser.find_element(*MainPageLocators.Title)
        title = n.text
        x = self.browser.find_element(*MainPageLocators.Title_assert)
        title2 = x.text
        assert title in title2 , 'Названия книг не совпадают'

    def cost(self):
        a = self.browser.find_element(*MainPageLocators.Main_Price)
        main_price = a.text
        b = self.browser.find_element(*MainPageLocators.Price_assert)
        allert_price = b.text
        c = self.browser.find_element(*MainPageLocators.Price_basket)
        basket_price = c.text
        assert main_price in allert_price, 'Стоимость алёрта и стоимость книги не совпадает'
        assert main_price in basket_price, 'Стоимость в корзине и стоимость товара не совпадают'

