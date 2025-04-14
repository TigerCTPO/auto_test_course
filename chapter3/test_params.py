import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)

    WebDriverWait(browser, 7).until(EC.element_to_be_clickable((By.ID, "ember466")))

    login = browser.find_element(By.ID, "ember466")
    login.click()

    time.sleep(2)

    email = browser.find_element(By.ID, "id_login_email")
    email.send_keys("qwerasdfgzxcv20@gmail.com")

    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("tiger2004")

    l_button = browser.find_element(By.CSS_SELECTOR, "#login_form > button")
    l_button.click()

    time.sleep(7)

    input = browser.find_element(By.TAG_NAME, "textarea")
    input.send_keys(math.log(int(time.time())))

    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()

    time.sleep(3)

    text = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert text == "Correct!"
