from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    link = "https://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "label span:nth-child(2)")
    x = x_element.text

    res = calc(x)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(res)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()