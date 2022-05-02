import pytest
from time import sleep
from Pages.searchPage import SearchPage


@pytest.mark.usefixtures("init_driver")
class Testsearch:

    def test_searchResults(self):
        searchPage = SearchPage(self.driver)
        searchPage.go_to_searchPage()
        sleep(3)
        searchPage.sendText_searchBox("lewis")
        searchPage.checknextPageLink()
        searchPage.checknextPageLink()
        searchPage.change_window_size(400, 756)
        sleep(3)
        searchPage.screenshot("mobileview.png")
