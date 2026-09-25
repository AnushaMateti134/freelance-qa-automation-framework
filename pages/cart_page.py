from playwright.sync_api import Page, expect
from utils.logger import get_logger

logger = get_logger(__name__)

class CartPage:

    def __init__(self, page: Page):
        self.page = page

        # Cart items
        self.cart_items = page.locator(".cart_item")

        # Product names
        self.cart_item_names = page.locator(
            ".inventory_item_name"
        )

        # Product quantities
        self.cart_item_quantities = page.locator(
            ".cart_quantity"
        )

        # Checkout button
        self.checkout_button = page.get_by_role(
            "button",
            name="Checkout"
        )

        # Continue shopping button
        self.continue_shopping_button = page.get_by_role(
            "button",
            name="Continue Shopping"
        )

    def get_item_count(self):
        return self.cart_items.count()

    def wait_for_item_count(self, expected_count):
        expect(
            self.cart_items
        ).to_have_count(expected_count)

    def get_cart_item(self, product_name):
        return self.cart_items.filter(
            has_text=product_name
        )

    def get_item_names(self):
        return self.cart_item_names.all_inner_texts()

    def get_item_quantity(self, product_name):
        item = self.get_cart_item(product_name)

        return item.locator(
            ".cart_quantity"
        ).inner_text()

    def proceed_to_checkout(self):

        expect(
            self.checkout_button
        ).to_be_visible()

        expect(
            self.checkout_button
        ).to_be_enabled()

        self.checkout_button.click()

        expect(
            self.page
        ).to_have_url(
            "https://www.saucedemo.com/checkout-step-one.html"
        )

    def proceed_to_checkout(self):
        logger.info("Proceeding to checkout")

        expect(self.checkout_button).to_be_visible()
        expect(self.checkout_button).to_be_enabled()

        self.checkout_button.click()