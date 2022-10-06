import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class test_class_name(unittest.TestCase):
    
    def test_registration1(self):
        
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
    
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//div[1]/input[@required]")
        input1.send_keys("John")
        input1 = browser.find_element(By.XPATH, "//div[2]/input[@required]")
        input1.send_keys("Konor")
        input1 = browser.find_element(By.XPATH, "//div[3]/input[@required]")
        input1.send_keys("Terminator900@gmail.com")
    
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
    
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
    
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

            
    def test_registration2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
    
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//div[1]/input[@required]")
        input1.send_keys("John")
        input1 = browser.find_element(By.XPATH, "//div[2]/input[@required]")
        input1.send_keys("Konor")
        input1 = browser.find_element(By.XPATH, "//div[3]/input[@required]")
        input1.send_keys("Terminator900@gmail.com")
    
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
    
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
    
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

        
if __name__ == "__main__": unittest.main()