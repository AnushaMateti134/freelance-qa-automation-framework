# Freelance QA Automation Framework

## Overview

A Python-based UI automation framework built using Playwright
and Pytest for testing the SauceDemo e-commerce application.

## Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model
- GitHub Actions
- Excel Reporting
- HTML Reporting

## Framework Architecture

pages/
tests/
test_data/
config/
utils/
reports/

freelance-qa-automation-framework/
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│
├── config/
│   └── settings.py
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── checkout_overview_page.py
│
├── test_data/
│   ├── login_data.py
│   ├── product_data.py
│   ├── checkout_data.py
│   └── saucedemo_complete_test_case_master.xlsx
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_e2e_shopping.py
│   └── test_smoke.py
│
├── utils/
│   ├── excel_reporter.py
│   ├── helpers.py
│   ├── logger.py
│   └── waits.py
│
├── reports/
│   ├── report.html
│   └── test_results.xlsx
│
├── test_results/
│   ├── screenshots/
│   ├── traces/
│   └── videos/
│
├── .env
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md

## Testing Coverage

- Functional Testing
- Smoke Testing
- Regression Testing
- Negative Testing
- Data-Driven Testing
- End-to-End Testing

## Automated Scenarios

- Login validation
- Product selection
- Product sorting
- Cart validation
- Checkout validation
- Required-field validation
- End-to-end shopping workflow

## Reporting

The framework generates:

- HTML test reports
- Excel execution reports
- Execution summary
- Module-wise test results

## How to Run

pip install -r requirements.txt

playwright install

pytest -v

## Author

Anusha Mateti