import pytest
from selenium import webdriver
from pagerss.product_page import ProductPage  # <--- ИЗМЕНЕНО ЗДЕСЬ

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    
    page = ProductPage(browser, link)
    page.open()
    
    page.add_to_basket()
    page.should_be_message_about_adding()
    page.should_be_cart_price_matching_product_price()