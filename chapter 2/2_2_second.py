from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "label span:nth-child(2)")
    x = x_element.text

    res = calc(x)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(res)

    browser.execute_script("window.scrollBy(0, 100);")

    option1 = browser.find_element(By.CLASS_NAME, "form-check-label")
    option1.click()

    browser.execute_script("window.scrollBy(0, 100);")

    option2 = browser.find_element(By.CSS_SELECTOR, "[class='form-check form-radio-custom'] > label")
    option2.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()