import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Функция из задания
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    # 1. Открываем страницу
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # 2. Считываем значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # 3. Считаем математическую функцию от x
    y = calc(x)

    # 4 и 5. Прокручиваем страницу к текстовому полю и вводим ответ
    input_field = browser.find_element(By.ID, "answer")
    # Используем execute_script, чтобы прокрутить именно к этому элементу
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
    input_field.send_keys(y)

    # 6. Прокручиваем к чекбоксу и выбираем "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    # 7. Прокручиваем к радиокнопке и переключаем "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    # 8. Прокручиваем к кнопке и нажимаем "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    # --- Получаем ответ из всплывающего окна ---
    time.sleep(1) # Небольшая пауза, чтобы окно успело появиться
    alert = browser.switch_to.alert
    alert_text = alert.text
    
    print("\n" + "="*50)
    print(f"Ваш ответ для Stepik: {alert_text}")
    print("="*50 + "\n")
    
    alert.accept() # Закрываем окно

finally:
    time.sleep(10) # Оставляем браузер открытым на 10 секунд, чтобы вы увидели результат
    browser.quit()