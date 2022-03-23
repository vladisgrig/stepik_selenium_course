import math
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_ufo_message(browser, link):
    browser.get(link)
    answer = str(math.log(int(time.time() - 122)))
    input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )
    input.send_keys(answer)
    
    button = browser.find_element(By.CSS_SELECTOR, "button[class='submit-submission']")
    button.click()

    hint = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "pre[class='smart-hints__hint']"))
    )
    hint_text = hint.text
    assert hint_text == "Correct!", f"Некорректный текст результата: {hint_text}, ожидается: Correct!"
    
