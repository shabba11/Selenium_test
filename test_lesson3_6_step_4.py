from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import math

def calculate():
    return str(math.log(int(time.time())))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize("url", [("https://stepik.org/lesson/236895/step/1"), ("https://stepik.org/lesson/236896/step/1"), ("https://stepik.org/lesson/236897/step/1"), ("https://stepik.org/lesson/236898/step/1"), ("https://stepik.org/lesson/236899/step/1"), ("https://stepik.org/lesson/236903/step/1"), ("https://stepik.org/lesson/236904/step/1"), ("https://stepik.org/lesson/236905/step/1")])
def test_message(browser, url):
    link = url
    browser.get(link)
    browser.implicitly_wait(10)
    text_area = browser.find_element(By.CLASS_NAME, "ember-text-area")
    text_area.send_keys(calculate())
    browser.implicitly_wait(5)
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    browser.implicitly_wait(5)
    correct_item = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert 'Correct!' in correct_item

