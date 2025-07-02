import pytest

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self,driver):     # <-- driver comes from conftest.py
        self.driver = driver