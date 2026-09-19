
import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


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
