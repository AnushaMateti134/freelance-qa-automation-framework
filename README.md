# Freelance QA Automation Framework for E-commerce Application

A Python-based UI test automation framework built with Playwright and Pytest.

This project is designed as a reusable automation framework for web application testing, with a focus on maintainability, scalability, reusable Page Objects, test data management, logging, reporting, and CI/CD integration.

---

# Tech Stack

- Python
- Playwright
- Pytest
- pytest-html
- Git
- GitHub
- GitHub Actions

---

## 📁 Project Structure

```text
freelance-qa-automation-framework/
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
│   └── checkout_data.py
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
│   ├── helpers.py
│   ├── logger.py
│   └── waits.py
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
