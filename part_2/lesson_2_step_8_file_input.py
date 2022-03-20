from selenium import webdriver
import os 
import time

current_dir = os.path.abspath(os.path.dirname(__file__)) 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Мой ответ")

    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Мой ответ")

    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("Мой ответ")

    file_path = os.path.join(current_dir, 'example.txt')
    file_input = browser.find_element_by_css_selector("#file")
    file_input.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()