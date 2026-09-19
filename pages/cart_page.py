
from playwright.sync_api import Page, Locator


class CartPage:
    """Page Object for the SauceDemo shopping cart."""

    def __init__(self, page: Page):
        self.page = page

        # Page locators
        self.cart_items: Locator = page.locator(
            ".cart_item"
        )
        self.cart_item_names: Locator = page.locator(
            ".inventory_item_name"
        )
        self.continue_shopping_button: Locator = page.get_by_role(
            "button", name="Continue Shopping"
        )
        self.checkout_button: Locator = page.get_by_role(
            "button", name="Checkout"
        )

    def get_item_count(self) -> int:
        """Return the number of distinct cart rows."""
        return self.cart_items.count()

    def get_item_names(self) -> list[str]:
        """Return the names of products in the cart."""
        return self.cart_item_names.all_inner_texts()

    def get_cart_item(self, product_name: str) -> Locator:
        """Return a cart row for a specific product."""
        return self.cart_items.filter(
            has=self.page.get_by_text(
                product_name, exact=True
            )
        ).first

    def get_item_quantity(self, product_name: str) -> str:
        """Return the displayed quantity for a product."""
        item = self.get_cart_item(product_name)

        return item.locator(
            ".cart_quantity"
        ).inner_text()

    def remove_product(self, product_name: str):
        """Remove a specific product from the cart."""
        item = self.get_cart_item(product_name)

        item.get_by_role(
            "button", name="Remove"
        ).click()

    def continue_shopping(self):
        """Return to the inventory page."""
        self.continue_shopping_button.click()

    def proceed_to_checkout(self):
        """Open the checkout page."""
        self.checkout_button.click()
