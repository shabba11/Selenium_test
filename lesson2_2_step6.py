from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def func(z):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element(By.ID, "input_value").text
y = func(x)
print(y)

input_id = browser.find_element(By.ID, "answer").send_keys(y)

browser.execute_script("window.scrollBy(0, 100);")

browser.find_element(By.ID, "robotCheckbox").click()
browser.find_element(By.ID, "robotsRule").click()

browser.find_element(By.CLASS_NAME, "btn-primary").click()