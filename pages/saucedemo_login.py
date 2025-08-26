from playwright.sync_api import Page
    
    
class LoginPage:
    def __init__(self,page:Page):
        self.page = page   
        self.username = page.locator("[data-test=\"username\"]")
        self.password = page.locator("[data-test=\"password\"]")
        self.loginbtn = page.locator("[data-test=\"login-button\"]")
        
    def enter_username(self, username:str):
        self.username.fill(username)    
        
    def enter_password(self,password:str):
        self.password.fill(password)    
     
    def click_login(self):
        self.loginbtn.click()    