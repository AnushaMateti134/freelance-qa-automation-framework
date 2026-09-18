
from playwright.sync_api import Page, Locator


class LoginPage:
    """Page Object for the SauceDemo login page."""

    def __init__(self, page: Page):
        self.page = page

        # Page locators
        self.username_input: Locator = page.locator("#user-name")
        self.password_input: Locator = page.locator("#password")
        self.login_button: Locator = page.locator("#login-button")
        self.error_message: Locator = page.locator(
            '[data-test="error"]'
        )

    def open(self, url: str):
        """Navigate to the login page."""
        self.page.goto(url)

    def enter_username(self, username: str):
        """Enter the username."""
        self.username_input.fill(username)

    def enter_password(self, password: str):
        """Enter the password."""
        self.password_input.fill(password)

    def click_login(self):
        """Click the Login button."""
        self.login_button.click()

    def login(self, username: str, password: str):
        """Perform the complete login workflow."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        """Return the login error message text."""
        return self.error_message.inner_text()