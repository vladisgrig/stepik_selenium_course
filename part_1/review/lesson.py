from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element_by_css_selector('.first_block .first')
    input_first_name.send_keys('Mykl')
    input_last_name = browser.find_element_by_css_selector('.first_block .second')
    input_last_name.send_keys('Knyazev')
    input_email = browser.find_element_by_css_selector('.first_block .third')
    input_email.send_keys('Knyazev@yandex.ru')

    input_phone = browser.find_element_by_css_selector('.second_block .first')
    input_phone.send_keys('+7 932 434 45 21')
    input_address = browser.find_element_by_css_selector('.second_block .second')
    input_address.send_keys('Izevsk')

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
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
