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
    browser.get("http://suninjuly.github.io/get_attribute.html")

    # 2. Находим на ней элемент-картинку (сундук)
    # У сундука на этой странице обычно id="treasure"
    treasure = browser.find_element(By.ID, "treasure")

    # 3. Взять у этого элемента значение атрибута valuex
    x = treasure.get_attribute("valuex")

    # 4. Посчитать математическую функцию от x
    y = calc(x)

    # 5. Ввести ответ в текстовое поле (id="answer")
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # 6. Отметить checkbox "I'm the robot" (id="robotCheckbox")
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # 7. Выбрать radiobutton "Robots rule!" (id="robotsRule")
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # 8. Нажать на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # --- Дополнительно ---
    # Ждем 1 секунду, чтобы всплывающее окно (alert) точно появилось
    time.sleep(1) 
    
    # Переключаемся на всплывающее окно и забираем из него текст
    alert = browser.switch_to.alert
    alert_text = alert.text
    
    # Печатаем ответ в консоль, чтобы вы могли его скопировать
    print("\n" + "="*50)
    print(f"Ваш ответ для вставки в Stepik: {alert_text}")
    print("="*50 + "\n")
    
    # Закрываем всплывающее окно
    alert.accept()

finally:
    # Оставляем браузер открытым на 10 секунд, чтобы вы увидели результат,
    # затем скрипт закроет его.
    time.sleep(10)
    browser.quit()