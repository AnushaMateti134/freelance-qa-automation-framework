
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_cart_contains_selected_product(
    logged_in_inventory: InventoryPage,
    cart_page: CartPage,
):
    inventory_page = logged_in_inventory

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )
    inventory_page.open_cart()

    expect(cart_page.page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )

    expect(
        cart_page.get_cart_item("Sauce Labs Backpack")
    ).to_be_visible()



def test_cart_contains_multiple_products(
    logged_in_inventory: InventoryPage,
    cart_page: CartPage,
):
    inventory_page = logged_in_inventory

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )
    inventory_page.add_product_to_cart(
        "Sauce Labs Bike Light"
    )

    inventory_page.open_cart()

    cart_page.wait_for_item_count(2)

    assert cart_page.get_item_count() == 2

def test_cart_product_names(
    logged_in_inventory: InventoryPage,
    cart_page: CartPage,
):
    inventory_page = logged_in_inventory

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )
    inventory_page.add_product_to_cart(
        "Sauce Labs Bike Light"
    )

    inventory_page.open_cart()

    product_names = cart_page.get_item_names()

    assert "Sauce Labs Backpack" in product_names
    assert "Sauce Labs Bike Light" in product_names
    assert len(product_names) == 2

def test_cart_product_quantity(
    logged_in_inventory: InventoryPage,
    cart_page: CartPage,
):
    inventory_page = logged_in_inventory

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )
    inventory_page.open_cart()

    assert cart_page.get_item_quantity(
        "Sauce Labs Backpack"
    ) == "1"

