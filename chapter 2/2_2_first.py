from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "h2 span:nth-child(2)")
    x = x_element.text

    y_element = browser.find_element(By.CSS_SELECTOR, "h2 span:nth-child(4)")
    y = y_element.text

    sum = int(x) + int(y)
    print(sum)

    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{sum}']").click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    

finally:
    time.sleep(10)
    browser.quit()