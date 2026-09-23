import pytest
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from test_data.checkout_data import INVALID_CHECKOUT_DATA

from playwright.sync_api import expect
@pytest.mark.parametrize(
    "first_name,last_name,postal_code,expected_error",
    INVALID_CHECKOUT_DATA
)
def test_checkout_required_fields(
    logged_in_inventory,
    page,
    first_name,
    last_name,
    postal_code,
    expected_error
):
    inventory_page = logged_in_inventory

    # Add product
    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    # Open cart
    inventory_page.open_cart()

    # Go to checkout
    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    # Enter checkout information
    checkout_page = CheckoutPage(page)

    checkout_page.enter_first_name(first_name)
    checkout_page.enter_last_name(last_name)
    checkout_page.enter_postal_code(postal_code)

    # Click Continue
    checkout_page.click_continue()

    # Verify validation message
    expect(
        checkout_page.get_error_message()
    ).to_be_visible()

    # Verify exact error message
    expect(
        checkout_page.get_error_message()
    ).to_have_text(expected_error)