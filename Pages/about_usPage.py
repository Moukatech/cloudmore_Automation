from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class AboutUsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.company_logo = (By.XPATH, "//*[@id ='hs-link-module_14891423382401005']/img")
        self.aboutUs_link = (By.XPATH, "//*[@id='hs_menu_wrapper_module_146731076570911']/ul/li[3]/a")
    
    def go_to_aboutUsPage(self):
        self.do_click(self.aboutUs_link)

    def assert_company_Logo (self):
        self.get_element(self.company_logo)
    
    def assert_page_title(self):
        self.get_title("About Us")
