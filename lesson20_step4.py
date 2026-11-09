import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistration(unittest.TestCase):
    
    def test_registration1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Иван")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Иванов")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("test@test.ru")
        
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Текст не совпадает")
        browser.quit()

    def test_registration2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Иван")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Иванов")
        # На этой странице нет поля .third, поэтому здесь возникнет ошибка NoSuchElementException
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("test@test.ru")
        
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Текст не совпадает")
        browser.quit()

if __name__ == "__main__":
    unittest.main()