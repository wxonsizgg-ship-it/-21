import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Функция для капчи
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    # 1. Открываем страницу
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # 2. Нажимаем на кнопку, которая открывает новую вкладку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Небольшая пауза, чтобы новая вкладка успела открыться
    time.sleep(1)

    # 3. Переключаемся на новую вкладку
    # browser.window_handles возвращает список всех открытых окон/вкладок
    # [0] - это первая (исходная) вкладка, [1] - новая вкладка
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # 4. Проходим капчу на новой вкладке
    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    
    # Считаем функцию
    y = calc(x)

    # Вводим ответ
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
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