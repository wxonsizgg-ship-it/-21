#Извините за кривой код, мне просто нужно набрать баллы, шобы мне автомат поставили по экзамену(

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[2]/input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.CLASS_NAME, "form-control.first")
    input4.send_keys("88005552555")
    input5 = browser.find_element(By.CLASS_NAME, "form-control.second")
    input5.send_keys("Пушкина")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    link = "http://suninjuly.github.io/registration2.html"

    time.sleep(5)
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'asdsad')
    input1.send_keys("Ivan")


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла