import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Стандартная функция для капчи
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    # 1. Открываем страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # 2. Ждем, когда цена дома уменьшится до $100
    # Задаем максимальное время ожидания 15 секунд (по условию не меньше 12)
    wait = WebDriverWait(browser, 15)
    
    # Ждем, пока в элементе с id="price" не появится текст "$100"
    wait.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 3. Нажимаем на кнопку "Book"
    # Делаем это сразу после того, как дождались нужной цены
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # 4. Решаем математическую задачу
    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    
    # Считаем функцию
    y = calc(x)

    # Вводим ответ
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Нажимаем кнопку Submit (на этой странице у неё id="solve")
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # --- Получаем ответ из всплывающего окна ---
    time.sleep(1) 
    alert = browser.switch_to.alert
    alert_text = alert.text
    
    print("\n" + "="*50)
    print(f"Ваш ответ для вставки в Stepik: {alert_text}")
    print("="*50 + "\n")
    
    # Закрываем окно
    alert.accept()

finally:
    # Оставляем браузер открытым на 10 секунд
    time.sleep(10)
    browser.quit()