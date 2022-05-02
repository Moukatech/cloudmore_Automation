import pytest
from time import sleep
from Pages.blogPage import BlogPage


@pytest.mark.usefixtures("init_driver")
class TestPlatform:

    def test_companyLogo(self):
        blogPage = BlogPage(self.driver)
        blogPage.go_to_blogPage()
        sleep(5)
        blogPage.assert_page_title()
        blogPage.assert_company_Logo()
        
