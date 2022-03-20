from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import os 
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

    time.sleep(1)

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(1)

    x_input = browser.find_element(By.ID, "input_value")
    x = x_input.text

    result = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(result)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()