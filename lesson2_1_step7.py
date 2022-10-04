from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    sunduk = browser.find_element(By.ID, "treasure")
    sunduk_valuex = sunduk.get_attribute("valuex")
    y = calc(sunduk_valuex)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CLASS_NAME, "btn-default").click()



finally:
    time.sleep(30)
    browser.quit()




