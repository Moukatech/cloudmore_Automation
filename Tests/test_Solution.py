
import pytest
from time import sleep
from Pages.solutionPage import SolutionPage


@pytest.mark.usefixtures("init_driver")
class TestSolution:

    def test_companyLogo(self):
        solutionPage = SolutionPage(self.driver)
        solutionPage.go_to_solutionPage()
        sleep(5)
        solutionPage.assert_page_title()
        solutionPage.assert_company_Logo()
