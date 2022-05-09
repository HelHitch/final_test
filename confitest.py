import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    print('---> Open browser')
    browser = webdriver.Chrome()
    yield browser
    print('---> Close Browser')
    browser.quit()
