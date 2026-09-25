
from playwright.sync_api import expect
from utils.logger import get_logger

logger = get_logger(__name__)

class InventoryPage:
    """Page Object for the SauceDemo inventory page."""

    def __init__(self, page: Page):
        self.page = page

        # Page locators
        self.page_title: Locator = page.get_by_text(
            "Products", exact=True
        )
        self.product_items: Locator = page.locator(
            ".inventory_item"
        )
        self.cart_link: Locator = page.locator(
            ".shopping_cart_link"
        )
        self.cart_badge: Locator = page.locator(
            ".shopping_cart_badge"
        )
        self.sort_dropdown: Locator = page.locator(
            ".product_sort_container"
        )

    def get_product_count(self) -> int:
        """Return the number of products displayed."""
        return self.product_items.count()

    def get_product(self, product_name: str) -> Locator:
        """Return a product card matching the given name."""
        return self.product_items.filter(
            has_text=product_name
        ).filter(
            has=self.page.get_by_text(
                product_name, exact=True
            )
        ).first

    def add_product_to_cart(self, product_name: str):
        """Add a specific product to the cart."""
        product = self.get_product(product_name)

        product.get_by_role(
            "button", name="Add to cart"
        ).click()

    def remove_product_from_cart(self, product_name: str):
        """Remove a specific product from the cart."""
        product = self.get_product(product_name)

        product.get_by_role(
            "button", name="Remove"
        ).click()

    def get_cart_count(self) -> int:
        """Return the cart badge count.

        Return 0 when the badge is not visible.
        """
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())

        return 0

    def open_cart(self):
        """Open the shopping cart."""
        self.cart_link.click()
        expect(self.page).to_have_url(
        "https://www.saucedemo.com/cart.html"
        )
    def sort_by(self, sort_value: str):
        """Sort products using a native select dropdown."""
        self.sort_dropdown.select_option(sort_value)
    def continue_to_overview(self):

        expect(
        self.continue_button
    ).to_be_visible()

        expect(
        self.continue_button
    ).to_be_enabled()

        self.continue_button.click()

        expect(
        self.page
    ).to_have_url(
        "https://www.saucedemo.com/checkout-step-two.html"
    )
    def get_error_message(self):
        return self.page.get_by_role("alert")

    def add_product_to_cart(self, product_name):
        logger.info(f"Adding product to cart: {product_name}")

        product = self.get_product(product_name)
        product.get_by_role("button", name="Add to cart").click()

    def sort_by(self, value):
        logger.info(f"Sorting products by: {value}")
        self.sort_dropdown.select_option(value)