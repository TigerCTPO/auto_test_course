import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_guest_should_see_add_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    time.sleep(5)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button is not None, "Кнопка не найдена на странице"


