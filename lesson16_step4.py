import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Стандартная функция для капчи
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    # 1. Открываем страницу
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # 2. Нажимаем на кнопку (на этой странице она одна, используем CSS-селектор)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 3. Принимаем confirm (нажимаем "ОК" во всплывающем окне)
    confirm = browser.switch_to.alert
    confirm.accept()

    # Небольшая пауза, чтобы новая страница точно успела загрузиться
    time.sleep(0.5) 

    # 4. Решаем капчу на новой странице
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

    # --- Получаем ответ из финального всплывающего окна ---
    time.sleep(1) 
    alert = browser.switch_to.alert
    alert_text = alert.text
    
    print("\n" + "="*50)
    print(f"Ваш ответ для вставки в Stepik: {alert_text}")
    print("="*50 + "\n")
    
    # Закрываем финальное окно
    alert.accept()

finally:
    # Оставляем браузер открытым на 10 секунд, чтобы вы увидели результат
    time.sleep(10)
    browser.quit()