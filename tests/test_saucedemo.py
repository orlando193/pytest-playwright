
from playwright.sync_api import Page, expect
from pages.saucedemo_login import LoginPage
from pages.saucedemo_home_page import HomePage


import pages.saucedemo_login as mod
print("Loaded from:", mod.__file__)
print("Has LoginPage:", hasattr(mod, "LoginPage"))

def test_example(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)

    page.goto("https://www.saucedemo.com/")
    
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    home_page.addtocart.click()
    home_page.cart.click()
    home_page.checkout.click()
    
    home_page.FN("orlando")
    home_page.LN("orlando")
    home_page.PC("12345")
    home_page.cont.click()
    home_page.finish.click()
    expect(home_page.check_finish).to_contain_text("Checkout: Complete!")
    home_page.logout()
    
    
   
    
    
    
