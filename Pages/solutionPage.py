from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class SolutionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.company_log = (By.XPATH, "//*[@id ='hs-link-module_14891423382401005']/img")
        self.solution_link = (By.XPATH, "//*[@id='hs_menu_wrapper_module_146731076570911']/ul/li[2]/a")
    
    def go_to_solutionPage(self):
        self.do_click(self.solution_link)

    def assert_company_Logo (self):
        self.get_element(self.company_log)
    
    def assert_page_title(self):
        self.get_title("Solutions")
