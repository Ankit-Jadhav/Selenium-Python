
# ✅ Which framework do you use?
# Pytest with Selenium
# Page Object Model (POM)
# Optional: Allure for reports, Jenkins for CI/CD
'''
# ✅ @pytest.markers - Used to tag tests.

import pytest

@pytest.mark.smoke
def test_login():
    assert True

@pytest.mark.regression
def test_add_item():
    assert True

"""🧠 Interview-Ready Answer:
Pytest markers allow me to group and filter tests. For example, I use @pytest.mark.smoke to tag smoke tests and run them separately using the -m option. This helps manage large test suites efficiently."""

✅ How to Run Marked Tests
Use -m in the command line:
pytest -m "smoke"

To run both smoke and regression:
pytest -m "smoke or regression" 


✅ -k and -m
Run selected tests:
pytest -k "login" → name contains "login"
pytest -m "smoke" → marked with @pytest.mark.smoke

✅ pytest-xdist & parallel mode
Run tests faster using multiple cores.
pytest -n 4  # 4 parallel workers

⚙️ MULTITHREADING
✅ threading and multithreading
Run multiple browser tests in parallel (less used in basic Selenium, better to use pytest-xdist).


fixtures?
conftest?
parameterization?
getter and setter?

'''

