import pytest
from time import sleep
from Pages.caseStudiesPage import CaseStudiesPage


@pytest.mark.usefixtures("init_driver")
class TestCaseStudies:

    def test_companyLogo(self):
        caseStudyPage = CaseStudiesPage(self.driver)
        caseStudyPage.go_to_caseStudyPage()
        sleep(5)
        caseStudyPage.assert_page_title()
        caseStudyPage.assert_company_Logo()
        
