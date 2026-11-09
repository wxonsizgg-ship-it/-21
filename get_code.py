import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

# Запускаем браузер
browser = webdriver.Chrome()

# Открываем страницу с багом (offer7)
browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7")

# Нажимаем "Добавить в корзину"
browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").click()

# Закрываем первое окно (ввод математики)
alert = browser.switch_to.alert
x = alert.text.split(" ")[2]
answer = str(math.log(abs((12 * math.sin(float(x))))))
alert.send_keys(answer)
alert.accept() 

# Ждем 1 секунду и ловим ВТОРОЕ окно (с кодом)
time.sleep(1) 
alert = browser.switch_to.alert
alert_text = alert.text

# ВЫВОДИМ КОД В ТЕРМИНАЛ (отсюда вы будете копировать)
print("\n" + "="*60)
print("ВАШ КОД (выделите мышкой в этом терминале и нажмите Ctrl+C):")
print(alert_text)
print("="*60 + "\n")

print("Скрипт заморожен. Окно в браузере не закроется само.")
print("Скопируйте код из этого терминала и вставьте на Stepik.")
print("После этого нажмите Ctrl+C в терминале (или просто закройте браузер и терминал).")

# СКРИПТ ЗАВИСАЕТ ЗДЕСЬ НАВСЕГДА (пока вы не нажмете Ctrl+C)
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    browser.quit()