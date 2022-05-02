import pytest
import allure
from selenium import webdriver
from config.config import TestData
from selenium.webdriver.common.by import By


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    web_driver.get(TestData.BASE_URL)
    web_driver.maximize_window()
    web_driver.find_element(By.ID, "hs-eu-confirmation-button").click()
    yield
    web_driver.close()
