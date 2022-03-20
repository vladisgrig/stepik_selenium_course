from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_input = browser.find_element(By.ID, "input_value")
    x = x_input.text

    result = calc(x)

    input = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    time.sleep(0.1)
    input.send_keys(result)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    time.sleep(0.1)    
    checkbox.click()

    radio_label = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)  
    time.sleep(0.1)      
    radio_label.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(0.1)    
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
