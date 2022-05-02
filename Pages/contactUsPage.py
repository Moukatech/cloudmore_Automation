from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class ContactUsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.company_log = (By.XPATH, "//*[@id ='hs-link-module_146731076570910']/img")
        self.contactUs_link = (By.XPATH, "//*[@id='hs_menu_wrapper_module_146731076570911']/ul/li[4]/a")
        self.contatUsForm = (By.ID, "hs_form_target_module_1422637098461108330")
        self.contatUsFooterForm = (By.ID, "hs_form_target_module_15009982909581442")
        
    
    def go_to_ContactUsPage(self):
        self.do_click(self.contactUs_link)

    def assert_company_Logo (self):
        self.get_element(self.company_log)
    
    def assert_page_title(self):
        self.get_title("Contact Us")
    
    def assert_form(self):
        self.get_element(self.contatUsForm)

    def assert_footer_form(self):
        self.get_element(self.contatUsFooterForm)