from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def formula(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

value_input = browser.find_element(By.ID, "input_value").text
value = formula(value_input)

browser.find_element(By.ID, "answer").send_keys(value)

browser.find_element(By.CLASS_NAME, "btn-primary").click()