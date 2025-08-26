from playwright.sync_api import Page 

class HomePage:
    def __init__(self, page:Page):
        self.page = page
        self.addtocart = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.cart = page.locator("[data-test=\"shopping-cart-link\"]")
        self.checkout = page.locator("[data-test=\"checkout\"]")
        self.firstname = page.locator("[data-test=\"firstName\"]")
        self.lastname = page.locator("[data-test=\"lastName\"]")
        self.postalcode = page.locator("[data-test=\"postalCode\"]")
        self.cont = page.locator("[data-test=\"continue\"]")
        self.finish = page.locator("[data-test=\"finish\"]")
        self.check_finish = page.locator('[data-test="title"]')
        
        self.openmenu = page.get_by_role("button", name="Open Menu")
        self.LO = page.locator("[data-test=\"logout-sidebar-link\"]")
        
    def checout(self):
        self.checkout.click()     
        
    def FN(self,firstname:str):
        self.firstname.fill(firstname)
        
    def LN(self,lastname:str):
        self.lastname.fill(lastname)
    
    def PC(self,postalcode:str):
        self.postalcode.fill(postalcode)    
        
    def complete(self):
        return self.check_finish
    
    def logout(self):
        self.openmenu.click()
        self.LO.click() 
        
            
            