from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    is_text_in_element = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5:nth-child(2)"), "$100"))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "label span:nth-child(2)")
    x = x_element.text

    res = calc(x)

    input1 = browser.find_element(By.TAG_NAME, "input:nth-child(2)")
    input1.send_keys(res)

    button = browser.find_element(By.TAG_NAME, "button:nth-child(2)")
    button.click()

finally:
    time.sleep(10)
    browser.quit()