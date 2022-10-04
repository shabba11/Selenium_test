from selenium import webdriver
from selenium.webdriver.common.by import By
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
print(file_path)

browser.find_element(By.NAME, "firstname").send_keys("Oleg")
browser.find_element(By.NAME, "lastname").send_keys("Olegovich")
browser.find_element(By.NAME, "email").send_keys("Oleg@oleg.ru")
browser.find_element(By.ID, "file").send_keys(file_path)

browser.find_element(By.CLASS_NAME, "btn-primary").click()