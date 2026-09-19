
from playwright.sync_api import Page, expect

from config.settings import BASE_URL, STANDARD_USER, PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_user_can_add_product_to_cart(page: Page):
    # Step 1: Login
    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    login_page.login(STANDARD_USER, PASSWORD)

    # Step 2: Create the inventory page object
    inventory_page = InventoryPage(page)

    expect(inventory_page.page_title).to_be_visible()

    # Step 3: Add a product
    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    # Step 4: Verify cart badge
    expect(inventory_page.cart_badge).to_have_text("1")

    # Step 5: Open cart
    inventory_page.open_cart()

    # Step 6: Create the cart page object
    cart_page = CartPage(page)

    # Step 7: Verify the selected product
    expect(
        cart_page.get_cart_item("Sauce Labs Backpack")
    ).to_be_visible()

    # Step 8: Verify quantity
    assert cart_page.get_item_quantity(
        "Sauce Labs Backpack"
    ) == "1"

def test_sort_products_high_to_low(
    logged_in_inventory: InventoryPage,
):
    inventory_page = logged_in_inventory

    inventory_page.sort_by("hilo")

    prices = inventory_page.page.locator(
        ".inventory_item_price"
    ).all_inner_texts()

    numeric_prices = [
        float(price.replace("$", ""))
        for price in prices
    ]

    assert numeric_prices == sorted(
        numeric_prices, reverse=True
    )
