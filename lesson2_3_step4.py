from http.client import OK
from ssl import AlertDescription
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def formula(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.CLASS_NAME, "btn-primary").click()

alert = browser.switch_to.alert
alert.accept()

value_input = browser.find_element(By.ID, "input_value").text
value = formula(value_input)

browser.find_element(By.ID, "answer").send_keys(value)

browser.find_element(By.CLASS_NAME, "btn-primary").click()