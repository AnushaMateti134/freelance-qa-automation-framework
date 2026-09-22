import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.checkout_overview_page import CheckoutOverviewPage
@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Provide a LoginPage object for each test."""
    return LoginPage(page)

import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from config.settings import BASE_URL, STANDARD_USER, PASSWORD


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def logged_in_inventory(
    page: Page,
    inventory_page: InventoryPage,
):
    """Log in and provide an inventory page."""
    login_page = LoginPage(page)

    login_page.open(BASE_URL)
    login_page.login(STANDARD_USER, PASSWORD)

    return inventory_page
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page)


@pytest.fixture
def checkout_overview_page(
    page: Page
) -> CheckoutOverviewPage:
    return CheckoutOverviewPage(page)
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from config.settings import BASE_URL, STANDARD_USER, PASSWORD


@pytest.fixture
def checkout_context(page: Page):
    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    login_page.login(STANDARD_USER, PASSWORD)

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