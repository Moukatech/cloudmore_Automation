from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.company_logo = (By.XPATH, "//*[@id='hs-link-module_14891423382401005']/img")
        # // *[ @ id = "hs-link-module_146731076570910"] / img
        self.platform_link = (By.XPATH, "//*[@id='hs_menu_wrapper_module_146731076570911']/ul/li[1]/a")
        self.solution_link = (By.XPATH, "//*[@id='hs_menu_wrapper_module_146731076570911']/ul/li[2]/a")
        self.about_us_link = (By.XPATH, "//*[@id='hs_menu_wrapper_module_146731076570911']/ul/li[3]/a")
        self.contactUs_link = (By.XPATH, "//*[@id='hs_menu_wrapper_module_146731076570911']/ul/li[4]/a")
        self.blog_link = (By.XPATH, "//*[@id='hs_menu_wrapper_module_146731076570911']/ul/li[5]/a")
        self.caseStudies_link = (By.XPATH, "//*[@id='hs_menu_wrapper_module_146731076570911']/ul/li[6]/a")
    def assert_company_Logo (self):
        self.get_element(self.company_logo)

    def assert_platform_link(self, element_text):
        self.get_element_text(self.platform_link, element_text)
    
    def assert_solution_link(self, element_text):
        self.get_element_text(self.solution_link, element_text)
    
    def assert_aboutUs_link(self, element_text):
        self.get_element_text(self.about_us_link, element_text) 
    
    def assert_contactUs_link(self, element_text):
        self.get_element_text(self.contactUs_link, element_text) 
    
    def assert_blog_link(self, element_text):
        self.get_element_text(self.blog_link, element_text)
    
    def assert_caseStudies_link(self, element_text):
        self.get_element_text(self.caseStudies_link, element_text) 