from faulthandler import is_enabled
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import pytest
class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_link = (By.XPATH, "//*[@id='hs_cos_wrapper_module_15306484973591482']/span")
        self.search_inputBox = (By.NAME, "term")
        self.search_button =(By.XPATH, "//*[@id='hs_cos_wrapper_module_1530555777115370']/div/form/button")
        self.next_PageLink =(By.XPATH, "//*[@id='hs_cos_wrapper_module_1530612174918208']//a[contains(text(),'Next page')]")
        self.previous_PageLink =(By.XPATH, "//*[@id='hs_cos_wrapper_module_1530612174918208']/div/div/a")
        self.no_searchResults = (By.CLASS_NAME, "hs-search__no-results")
    def go_to_searchPage(self):
        self.do_click(self.search_link)
    
    def sendText_searchBox(self, text):
        self.do_send_keys(self.search_inputBox, text)
        self.do_click(self.search_button)
        if self.no_searchResults:
            self.screenshot("No_Results.png")
            pytest.fail(f"No results found for searched word '{text}' ")
            
    
    def save_screenshot(self):
        self.screenshot()
    
    def change_size(self):
        self.change_window_size(400, 756)
    
    def checknextPageLink(self):
        if self.next_PageLink == True:
            self.scroll_to_element(self.next_PageLink)
            # self.do_click(self.next_PageLink)
        elif self.previous_PageLink:
            self.do_click(self.previous_PageLink)
            self.scroll_toThe_Top()
            self.screenshot("fullsize.png")
        else:
            self.do_click(self.previous_PageLink)
            self.screenshot("fullsize.png")

