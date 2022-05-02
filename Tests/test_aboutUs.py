
import pytest
from time import sleep
from Pages.about_usPage import AboutUsPage


@pytest.mark.usefixtures("init_driver")
class TestAboutUs:

    def test_companyLogo(self):
        aboutUsPage = AboutUsPage(self.driver)
        aboutUsPage.go_to_aboutUsPage()
        sleep(5)
        aboutUsPage.assert_page_title()
        aboutUsPage.assert_company_Logo()
