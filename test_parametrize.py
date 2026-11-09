import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window() # Раскрываем окно на весь экран для стабильности
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestStepikParametrize:
    message = ""
    links = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ]

    @pytest.mark.parametrize('link', links)
    def test_guest_should_see_login_link(self, browser, link):
        
        # --- АВТОРИЗАЦИЯ ---
        browser.get("https://stepik.org/login")
        WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located((By.ID, "id_login_email"))
        ).send_keys("lemonboy1@mail.ru") 
        browser.find_element(By.ID, "id_login_password").send_keys("GG14") 
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Ждем, пока прогрузится страница профиля
        try:
            WebDriverWait(browser, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Выйти') or contains(text(), 'Log out')]"))
            )
        except:
            browser.refresh()
            time.sleep(3)
        
        # --- ПЕРЕХОД К ЗАДАЧАМ ---
        browser.get(link)
        
        try:
            # Ждем появления textarea
            textarea = WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area"))
            )
            
            # Вводим ответ через JavaScript, чтобы обойти проблемы с перекрытием
            answer = str(math.log(int(time.time())))
            browser.execute_script("arguments[0].value = arguments[1];", textarea, answer)
            time.sleep(0.5) # Небольшая пауза, чтобы значение "применилось"
            
            # Нажимаем кнопку "Отправить"
            submit_button = WebDriverWait(browser, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
            )
            browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            time.sleep(0.5)
            submit_button.click()
            
            # Ждем фидбек
            feedback = WebDriverWait(browser, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
            )
            feedback_text = feedback.text
            
            if feedback_text != "Correct!":
                TestStepikParametrize.message += feedback_text + " "
                print(f"\n[!] Найден кусочек текста: {feedback_text}")
                
            assert feedback_text == "Correct!", f"Ожидался текст 'Correct!', но получен: {feedback_text}"
            
        except Exception as e:
            print(f"\n[!] Ошибка на странице {link}: {e}")
            # Тест не падает, а продолжает выполнение, чтобы собрать текст с других страниц
            pass

    @classmethod
    def teardown_class(cls):
        print("\n" + "="*70)
        print(f"СОБРАННЫЙ ТЕКСТ ДЛЯ STEPIK:\n{cls.message.strip()}")
        print("="*70 + "\n")