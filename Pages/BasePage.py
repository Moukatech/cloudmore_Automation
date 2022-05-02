from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        # self.driver.find_element_by_xpath(ele).click()
        ele=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].click();", ele)

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator, text):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        print (ele)
        assert text == ele

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
        
    def get_element(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(ele)
    
    def screenshot(self, name):
        self.driver.save_screenshot(name)

    def scroll_toThe_Top(self):
        self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + Keys.HOME)

    def change_window_size(self, width, height):
        self.scroll_toThe_Top()
        self.driver.set_window_size(width, height)
    
    def scroll_to_element(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        # action = ActionChains(self.driver)
        # action.move_to_element(ele).perform()
        self.driver.execute_script("arguments[0].click();", ele)

