
# Selenium Methods - Python with Selenium Interview Notes

## 1. Alert Handling

### 🔹 Case A: Basic Alert Handling

alert = driver.switch_to.alert
print(alert.text)
alert.accept()
alert.dismiss()

> ⚠️ If the alert is not present yet, it will throw a `NoAlertPresentException`.

### 🔹 Case B: Wait for Alert to Appear
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
alert = wait.until(EC.alert_is_present())
print(alert.text)
alert.accept()
```

---

## 2. Handling HTTP Auth Popups
```python
url = f"https://{username}:{password}@{host}"
driver.get(url)
```

---

## 3. Selenium Navigation Commands
```python
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
```

---

## 4. Bypass SSL Certificate Errors
```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.implicitly_wait(5)
```

---

## 5. Handle Cookies in Selenium

### 🔹 Fetch Cookies
```python
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))
```

### 🔹 Add a Cookie
```python
driver.add_cookie({"name": "Python", "value": "123agbcd"})
```

### 🔹 Loop Over Cookies
```python
for i in cookies:
    print(i)
```

### 🔹 Delete Specific Cookie by Name
```python
driver.delete_cookie("Python")
```

### 🔹 Delete All Cookies
```python
driver.delete_all_cookies()
```

---

## 6. Drag and Drop in Selenium
```python
from selenium.webdriver.common.action_chains import ActionChains

drag_me = driver.find_element(By.ID, "draggable")
drop_here = driver.find_element(By.ID, "droppable")

actions = ActionChains(driver)
actions.drag_and_drop(drag_me, drop_here).perform()
```

---

## 7. Selenium Dropdown Handling

### 🔹 Using Select Class (only for `<select>` tag)
```python
from selenium.webdriver.support.select import Select

dropdown_element = driver.find_element(By.ID, "element_of_select_tag")
select = Select(dropdown_element)

# Select Methods
select.select_by_visible_text("India")
select.select_by_value("India")
select.select_by_index(3)
```

### 🔹 Check if Multi-select
```python
print(select.is_multiple)  # Returns True or False
```

### ❌ Deselect (only for multi-select dropdowns)
```python
select.deselect_by_visible_text("India")
select.deselect_all()
```
