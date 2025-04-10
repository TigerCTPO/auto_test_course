from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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