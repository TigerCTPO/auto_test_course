import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block > div:nth-child(1) > input")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block > div:nth-child(2) > input")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block > div:nth-child(3) > input")
        input3.send_keys("Petrov@gmail.com")

        input4 = browser.find_element(By.CSS_SELECTOR, ".second_block > div:nth-child(1) > input")
        input4.send_keys("333")

        input5 = browser.find_element(By.CSS_SELECTOR, ".second_block > div:nth-child(2) > input")
        input5.send_keys("Russia")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Error1")
        
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block > div:nth-child(1) > input")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block > div:nth-child(2) > input")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block > div:nth-child(3) > input")
        input3.send_keys("Petrov@gmail.com")

        input4 = browser.find_element(By.CSS_SELECTOR, ".second_block > div:nth-child(1) > input")
        input4.send_keys("333")

        input5 = browser.find_element(By.CSS_SELECTOR, ".second_block > div:nth-child(2) > input")
        input5.send_keys("Russia")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Error2")
        
if __name__ == "__main__":
    unittest.main()