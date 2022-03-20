from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num_1 = browser.find_element(By.ID, "num1")
    x = int(num_1.text)

    num_2 = browser.find_element(By.ID, "num2")
    y = int(num_2.text)    

    result = x + y

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(result))

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
