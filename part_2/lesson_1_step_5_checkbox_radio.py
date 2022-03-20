from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_input = browser.find_element(By.ID, "input_value")
    x = x_input.text

    result = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(result)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio_label = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio_label.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
