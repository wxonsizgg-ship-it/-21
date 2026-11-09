import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Инициализируем браузер
browser = webdriver.Chrome()

try:
    # 1. Открываем страницу
    browser.get("https://suninjuly.github.io/selects1.html")

    # 2. Считываем значения заданных чисел
    # Находим первое число (обычно id="num1") и берем его текст
    num1 = browser.find_element(By.ID, "num1").text
    # Находим второе число (обычно id="num2") и берем его текст
    num2 = browser.find_element(By.ID, "num2").text

    # 3. Считаем сумму заданных чисел
    # Переводим текст в целые числа (int) и складываем
    total_sum = int(num1) + int(num2)

    # 4. Выбираем в выпадающем списке значение равное сумме
    # Находим сам выпадающий список по id="dropdown"
    dropdown_element = browser.find_element(By.ID, "dropdown")
    # Создаем объект Select для работы со списком
    select = Select(dropdown_element)
    
    # Выбираем значение по value. 
    # ВАЖНО: Метод select_by_value требует строку (str), 
    # поэтому преобразуем нашу сумму обратно в строку.
    select.select_by_value(str(total_sum))

    # 5. Нажимаем на кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # --- Перехват ответа для удобства ---
    time.sleep(1) 
    alert = browser.switch_to.alert
    alert_text = alert.text
    
    print("\n" + "="*50)
    print(f"Ваш ответ для вставки в Stepik: {alert_text}")
    print("="*50 + "\n")
    
    alert.accept()

finally:
    # Оставляем браузер открытым на 10 секунд, чтобы вы увидели результат
    time.sleep(10)
    browser.quit()