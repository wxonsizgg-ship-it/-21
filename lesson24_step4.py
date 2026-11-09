import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Список уроков из вашего задания
lessons = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]
full_message = []

print("Запуск браузера...")
driver = webdriver.Chrome()

try:
    for index, lesson in enumerate(lessons, 1):
        link = f"https://stepik.org{lesson}/step/1"
        driver.get(link)
        
        # Если это первая страница, даем время авторизоваться вручную, если нужно
        if index == 1:
            print("\n⚠️ ВНИМАНИЕ: Если вы не авторизованы в открывшемся браузере,")
            print("у вас есть 15 секунд, чтобы войти в свой аккаунт Stepik руками!")
            time.sleep(15)
        
        # 1. Ждем поле ввода
        textarea = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
        )
        textarea.clear()
        
        # 2. Считаем формулу и вставляем
        answer = str(math.log(int(time.time())))
        textarea.send_keys(answer)
        
        # 3. Кликаем «Отправить»
        submit_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        submit_btn.click()
        
        # 4. Получаем фидбек (слово)
        feedback_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_to_be_clickable((By.CSS_SELECTOR, ".smart-hints__feedback"))
        )
        
        word = feedback_element.text
        print(f"Ссылка {index}/8 ({lesson}): получено слово -> '{word}'")
        
        if word != "Correct!":
            full_message.append(word)
            
        # Небольшая пауза между запросами
        time.sleep(2)

    print("\n СБОР ФРАЗЫ ЗАВЕРШЕН!")
    print("Итоговое послание:", " ".join(full_message))

finally:
    driver.quit()