from selenium.common.exceptions import NoAlertPresentException
import pytest
from selenium.webdriver.common.by import By
import math
import time

class BasePage():
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        
    def add_product_to_basket(self, link):
        self.browser.get(link)
        button = self.browser.find_element(By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
        button.click()
        self.solve_quiz_and_get_code()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            time.sleep(4)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")