from .test_base import BaseTest
from ..pages.homePage import googleHomePage
from ..config.config import config
 

class testGoogle(BaseTest):
    def test_google_homepage(self):
        self.driver.get(config.BASE_URL)
        home = googleHomePage(self.driver)

        assert "Google" in home.get_title()
        assert home.verif_search_box()