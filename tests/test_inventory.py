
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage


def test_inventory_page_loads(
    logged_in_inventory: InventoryPage,
):
    inventory_page = logged_in_inventory

    expect(inventory_page.page_title).to_be_visible()

    expect(inventory_page.page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


def test_inventory_has_six_products(
    logged_in_inventory: InventoryPage,
):
    inventory_page = logged_in_inventory

    expect(inventory_page.product_items).to_have_count(6)


def test_add_single_product_to_cart(
    logged_in_inventory: InventoryPage,
):
    inventory_page = logged_in_inventory

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    expect(inventory_page.cart_badge).to_have_text("1")


def test_add_multiple_products_to_cart(
    logged_in_inventory: InventoryPage,
):
    inventory_page = logged_in_inventory

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )
    inventory_page.add_product_to_cart(
        "Sauce Labs Bike Light"
    )

    expect(inventory_page.cart_badge).to_have_text("2")


def test_remove_product_from_inventory(
    logged_in_inventory: InventoryPage,
):
    inventory_page = logged_in_inventory

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.remove_product_from_cart(
        "Sauce Labs Backpack"
    )

    expect(inventory_page.cart_badge).to_have_count(0)


def test_sort_products_by_price_low_to_high(
    logged_in_inventory: InventoryPage,
):
    inventory_page = logged_in_inventory

    inventory_page.sort_by("lohi")

    prices = inventory_page.page.locator(
        ".inventory_item_price"
    ).all_inner_texts()

    numeric_prices = [
        float(price.replace("$", ""))
        for price in prices
    ]

    assert numeric_prices == sorted(numeric_prices)
