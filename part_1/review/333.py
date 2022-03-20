from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    a = browser.find_element_by_xpath("//input[@class='form-control first']")
    a.send_keys("Волан")
    time.sleep(1)
    b = browser.find_element_by_xpath("//input[@class='form-control second']")
    b.send_keys("Де-Морт")
    time.sleep(1)
    c = browser.find_element_by_xpath("//input[@class='form-control third' and @placeholder='Input your email']")
    c.send_keys("Hog@mail.ru")
    time.sleep(1)
    d = browser.find_element_by_xpath("//input[@class='form-control first' and @placeholder='Input your phone:']")
    d.send_keys("+1292939293")
    time.sleep(1)
    e = browser.find_element_by_xpath("//input[@class='form-control second' and @placeholder='Input your address:']")
    e.send_keys("Косая аллея")
    time.sleep(1)

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