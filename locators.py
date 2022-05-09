from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET = (By.CSS_SELECTOR, "[value = 'Add to basket']")