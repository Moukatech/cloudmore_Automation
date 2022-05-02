import pytest

from Pages.homePage import HomePage
# from Tests.test_base import BaseTest
from config.config import TestData


@pytest.mark.usefixtures("init_driver")
class TestHome:

    def test_companyLogo(self):
        home_page = HomePage(self.driver)
        home_page.assert_company_Logo()

    def test_platform_link(self):
        home_page = HomePage(self.driver)
        home_page.assert_platform_link("PLATFORM")

    def test_solution_link(self):
        home_page = HomePage(self.driver)
        home_page.assert_solution_link("SOLUTIONS")
    
    def test_AboutUs_link(self):
        home_page = HomePage(self.driver)
        home_page.assert_aboutUs_link("ABOUT US")
    
    def test_contactUs_link(self):
        home_page = HomePage(self.driver)
        home_page.assert_contactUs_link("CONTACT US")
    
    def test_blog_link(self):
        home_page = HomePage(self.driver)
        home_page.assert_blog_link("BLOG")
    
    def test_caseStudies_link(self):
        home_page = HomePage(self.driver)
        home_page.assert_caseStudies_link("CASE STUDIES")