from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
    input1.send_keys("first")
    input2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
    input2.send_keys("second")
    input3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
    input3.send_keys("third")


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
