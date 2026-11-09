import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# --- Подготовка файла ---
# Получаем текущую директорию, где лежит скрипт
current_dir = os.path.abspath(os.path.dirname(__file__))
# Формируем путь к файлу (файл будет называться upload_file.txt)
file_path = os.path.join(current_dir, 'upload_file.txt')

# Создаем пустой текстовый файл, если его еще нет
with open(file_path, 'w') as file:
    pass 

# Инициализируем браузер
browser = webdriver.Chrome()

try:
    # 1. Открываем страницу
    browser.get("http://suninjuly.github.io/file_input.html")

    # 2. Заполняем текстовые поля: имя, фамилия, email
    # Используем атрибут name для поиска полей
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Иван")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Иванов")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("test@example.com")

    # 3. Загружаем файл
    # Находим элемент input с типом file и передаем ему абсолютный путь к файлу
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # 4. Нажимаем на кнопку "Submit"
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

    # --- Уборка ---
    # (Опционально) Удаляем временный файл после завершения, чтобы не мусорить
    if os.path.exists(file_path):
        os.remove(file_path)