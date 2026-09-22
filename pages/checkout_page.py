from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.first_name_input = page.get_by_role(
            "textbox",
            name="First Name"
        )

        self.last_name_input = page.get_by_role(
            "textbox",
            name="Last Name"
        )

        self.postal_code_input = page.get_by_role(
            "textbox",
            name="Zip/Postal Code"
        )

        self.continue_button = page.get_by_role(
            "button",
            name="Continue"
        )

    def enter_first_name(self, first_name):
        self.first_name_input.fill(first_name)

    def enter_last_name(self, last_name):
        self.last_name_input.fill(last_name)

    def enter_postal_code(self, postal_code):
        self.postal_code_input.fill(postal_code)

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