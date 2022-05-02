import pytest
from time import sleep
from Pages.contactUsPage import ContactUsPage


@pytest.mark.usefixtures("init_driver")
class TestContactUs:

    def test_companyLogo(self):
        contactUsPage = ContactUsPage(self.driver)
        contactUsPage.go_to_ContactUsPage()
        sleep(5)
        contactUsPage.assert_page_title()
        contactUsPage.assert_company_Logo()
        contactUsPage.assert_form()
        contactUsPage.assert_footer_form()
