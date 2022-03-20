from selenium import webdriver
import time

try:
    #link1 и link2 - ссылки на первую и вторую страницы соответственно 
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link2)

    # Ваш код, который заполняет обязательные поля
    FirstName =  browser.find_element_by_css_selector(".first_block .first")
    FirstName.send_keys("Name")
    LastName =  browser.find_element_by_css_selector(".first_block .second")
    LastName.send_keys("Familya")
    Email =  browser.find_element_by_css_selector(".first_block .third")
    Email.send_keys("i@ you@")
    
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