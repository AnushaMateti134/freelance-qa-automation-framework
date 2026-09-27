import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage

from config.settings import BASE_URL, STANDARD_USER, PASSWORD
from utils.excel_reporter import create_excel_report


# ============================================================
# EXCEL TEST RESULT STORAGE
# ============================================================

test_results = []


def pytest_runtest_logreport(report):

    # Record normal test execution
    if report.when == "call":

        if report.passed:
            status = "PASS"
            error = ""

        elif report.failed:
            status = "FAIL"
            error = str(report.longrepr)

        elif report.skipped:
            status = "SKIP"
            error = ""

        else:
            status = "UNKNOWN"
            error = ""

    # Record fixture/setup errors
    elif report.when == "setup" and report.failed:

        status = "ERROR"
        error = str(report.longrepr)

    else:
        return

    test_results.append({
        "test_name": report.nodeid,
        "status": status,
        "duration": round(
            report.duration,
            2
        ),
        "error": error,
    })


def pytest_sessionfinish(
    session,
    exitstatus
):

    create_excel_report(
        test_results
    )
# PYTEST SESSION FINISH
# ============================================================

def pytest_sessionfinish(session, exitstatus):

    create_excel_report(test_results)


# ============================================================
# PAGE OBJECT FIXTURES
# ============================================================

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Provide a LoginPage object for each test."""
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    """Provide an InventoryPage object for each test."""
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    """Provide a CartPage object for each test."""
    return CartPage(page)


@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    """Provide a CheckoutPage object for each test."""
    return CheckoutPage(page)


@pytest.fixture
def checkout_overview_page(
    page: Page,
) -> CheckoutOverviewPage:
    """Provide a CheckoutOverviewPage object for each test."""
    return CheckoutOverviewPage(page)


# ============================================================
# LOGGED-IN INVENTORY FIXTURE
# ============================================================

@pytest.fixture
def logged_in_inventory(
    page: Page,
    inventory_page: InventoryPage,
):
    """Log in and provide an InventoryPage object."""

    login_page = LoginPage(page)

    login_page.open(BASE_URL)
    login_page.login(
        STANDARD_USER,
        PASSWORD
    )

    return inventory_page


# ============================================================
# COMPLETE CHECKOUT CONTEXT
# ============================================================

@pytest.fixture
def checkout_context(page: Page):

    login_page = LoginPage(page)

    login_page.open(BASE_URL)

    login_page.login(
        STANDARD_USER,
        PASSWORD
    )

    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    overview_page = CheckoutOverviewPage(page)

    return {
        "inventory": inventory_page,
        "cart": cart_page,
        "checkout": checkout_page,
        "overview": overview_page,
    }