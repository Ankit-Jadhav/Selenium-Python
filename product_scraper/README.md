# 🛍️ Product Scraper

A robust automation framework for scraping product details from web pages using Python, Selenium, and PyTest.

---

## 📁 Project Structure
product_scraper/
│
├── tests/                         # Test cases using pytest
│   └── test_product_page.py
│
├── pages/                         # POM files
│   └── product_page.py
│
├── utils/                         # Helpers & data handling
│   ├── data_collector.py
│   └── logger.py
│
├── logs/                          # Test logs
│   └── test_log_*.log
│
├── screenshots/                   # Screenshots on failure
│   └── test_failed_login.png
│
├── reports/                       # Pytest HTML or Allure report folder (optional)
│
├── allure-results/                # ✅ Auto-created: Raw Allure test output
├── conftest.py                    # Fixtures & screenshot hook
├── requirements.txt               # Dependencies
└── pytest.ini                     # Pytest config (optional)
└──README.md                       # Project overview and setup instructions



---

## ⚙️ Getting Started

### Install Dependencies


pip install -r requirements.txt

### Run Tests

pytest --alluredir=allure-results

### Generate Allure Report

allure serve allure-results

1. Project Prerequisites
## 🔧 Prerequisites

- Python 3.7+
- Google Chrome or Firefox (based on your driver)
- ChromeDriver or GeckoDriver added to your PATH
- Java installed (for Allure)

### 2. Environment Setup (Optional but Useful)
## 🛠️ Setup (Optional but Recommended)

# Create and activate a virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Then install dependencies
pip install -r requirements.txt


### 3. Example Test Command

## 🚀 Example Command to Run Tests with Allure

pytest tests/ --alluredir=allure-results
allure serve allure-results

### 4. Project Purpose (First paragraph clarification)

A robust automation framework for scraping and testing product information from web pages using Python, Selenium, and PyTest, built with maintainability and reporting in mind using the Page Object Model (POM) design pattern.







