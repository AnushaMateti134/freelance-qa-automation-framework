from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage


def test_complete_checkout_workflow(
    logged_in_inventory,
    page,
):

    # Step 1: Add product
    inventory_page = logged_in_inventory

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    # Step 2: Open cart
    inventory_page.open_cart()

    # Step 3: Create CartPage
    cart_page = CartPage(page)

    # Step 4: Wait for cart item
    cart_page.wait_for_item_count(1)

    # Step 5: Go to checkout
    cart_page.proceed_to_checkout()

    # Step 6: Create CheckoutPage
    checkout_page = CheckoutPage(page)

    # Step 7: Enter customer information
    checkout_page.enter_first_name("Anusha")
    checkout_page.enter_last_name("Mateti")
    checkout_page.enter_postal_code("12345")

    # Step 8: Continue to overview
    checkout_page.continue_to_overview()

    # Step 9: Create CheckoutOverviewPage
    overview_page = CheckoutOverviewPage(page)

    # Step 10: Verify subtotal
    expected_subtotal = (
        overview_page.calculate_subtotal_from_products()
    )

    actual_subtotal = (
        overview_page.get_item_total()
    )

    assert actual_subtotal == expected_subtotal

    # Step 11: Finish checkout
    overview_page.finish_checkout()