import time
import pytest
from selenium import webdriver
from pages.product_page import ProductPage

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    time.sleep(60)
    print("\nquit browser..")
    browser.quit()

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    
    expected_name = page.get_product_name()
    expected_price = page.get_product_price()
    
    page.add_to_basket()
    
    page.should_be_correct_success_message(expected_name, expected_price)