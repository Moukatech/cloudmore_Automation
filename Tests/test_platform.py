
import pytest
from time import sleep
from Pages.platformPage import PlatformPage


@pytest.mark.usefixtures("init_driver")
class TestPlatform:

    def test_companyLogo(self):
        platformPage = PlatformPage(self.driver)
        platformPage.go_to_PlatformPage()
        sleep(5)
        platformPage.assert_page_title()
        platformPage.assert_company_Logo()
