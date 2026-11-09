import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Функция для вычисления, как указано в задании
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Инициализируем браузер (по умолчанию используется Chrome)
browser = webdriver.Chrome()

try:
    # 1. Открываем страницу
    browser.get("https://suninjuly.github.io/math.html")

    # 2. Считываем значение для переменной x
    # На этой странице значение x находится в элементе с id="input_value"
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # 3. Считаем математическую функцию от x
    y = calc(x)

    # 4. Вводим ответ в текстовое поле (id="answer")
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # 5. Отмечаем checkbox "I'm the robot" (id="robotCheckbox")
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # 6. Выбираем radiobutton "Robots rule!" (id="robotsRule")
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # 7. Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # --- Дополнительно ---
    # Ждем 1 секунду, чтобы всплывающее окно (alert) точно появилось
    time.sleep(1) 
    
    # Переключаемся на всплывающее окно и забираем из него текст
    alert = browser.switch_to.alert
    alert_text = alert.text
    
    # Печатаем ответ в консоль, чтобы вы могли его скопировать
    print("\n" + "="*40)
    print(f"Ваш ответ для вставки в Stepik: {alert_text}")
    print("="*40 + "\n")
    
    # Закрываем всплывающее окно
    alert.accept()

finally:
    # Оставляем браузер открытым на 10 секунд, чтобы вы увидели результат,
    # затем скрипт закроет его.
    time.sleep(10)
    browser.quit()