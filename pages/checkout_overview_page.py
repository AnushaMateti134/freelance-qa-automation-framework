from playwright.sync_api import Page, expect

class CheckoutOverviewPage:

    def __init__(self, page: Page):
        self.page = page

        self.item_prices = page.locator(
            ".inventory_item_price"
        )

        self.item_total = page.locator(
            ".summary_subtotal_label"
        )

        self.finish_button = page.get_by_role(
            "button",
            name="Finish"
        )

    def calculate_subtotal_from_products(self):
        prices = self.item_prices.all_inner_texts()

        total = sum(
            float(price.replace("$", ""))
            for price in prices
        )

        return total

    def get_item_total(self):
        text = self.item_total.inner_text()

        return float(
            text.replace("Item total: $", "")
        )

    def finish_checkout(self):

        expect(
            self.finish_button
        ).to_be_visible()

        self.finish_button.click()

        expect(
            self.page
        ).to_have_url(
            "https://www.saucedemo.com/checkout-complete.html"
        )