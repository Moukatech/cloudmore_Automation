from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class BlogPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.company_log = (By.XPATH, "//*[@id ='hs-link-module_146731076570910']/img")
        self.blog_link = (By.XPATH, "//*[@id='hs_menu_wrapper_module_146731076570911']/ul/li[5]/a")
        
    
    def go_to_blogPage(self):
        self.do_click(self.blog_link)

    def assert_company_Logo (self):
        self.get_element(self.company_log)
    
    def assert_page_title(self):
        self.get_title("Cloudmore Blog")