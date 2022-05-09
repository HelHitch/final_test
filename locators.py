

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET = (By.CSS_SELECTOR, "[value = 'Add to basket']")
    Title = (By.XPATH, '//div/h1')
    Title_assert = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    Main_Price = (By.CSS_SELECTOR, "[class= 'price_color']")
    Price_assert = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    Price_basket = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs")
