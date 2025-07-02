#  Smoke + Regression test examples
import pytest 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ✅ SMOKE TEST: Just check homepage loads

@pytest.mark.smoke
def test_homepage_loads(browser):
    browser.get("https://www.hubspot.com/")
    assert "HubSpot" in browser.title\

# ✅ REGRESSION TEST: Check if 'Talk to Sales' button is present
@pytest.mark.regression
def test_select_a_language(browser):
    browser.get("https://www.hubspot.com/")

# Wait until at least one button is loaded
    WebDriverWait(browser,15).until(EC.presence_of_all_elements_located((By.TAG_NAME,"button")))

    #get all the buttons
    
    buttons = browser.find_elements(By.TAG_NAME, "button")
    texts = [" ".join(b.text.split()) for b in buttons if b.text.strip()]

    print("✅ Buttons found:", texts)


    assert "Select a language" in texts 


'''pytest -m smoke        # Smoke pipeline
pytest -m regression   # Full regression pipeline

pytest -m regression -s    The -s flag tells pytest to disable output capturing, so your print() statements will show in the terminal.
pytest -n 2  --- for two browser
pytest-xdist for parallel execution

pytest -m regression -n 3      Run regression tests in parallel across browsers:
 '''
