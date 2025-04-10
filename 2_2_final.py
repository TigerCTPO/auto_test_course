from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 



try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-group > [name='firstname']")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, ".form-group > [name='lastname']")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR, ".form-group > [name='email']")
    input3.send_keys("Petrov@gmail.com")

    element = browser.find_element(By.CSS_SELECTOR, "form > input")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
