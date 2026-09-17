
from playwright.sync_api import Page, expect

from config.settings import BASE_URL


def test_saucedemo_homepage_loads(page: Page):
    # Open the application
    page.goto(BASE_URL)

    # Verify the page title
    expect(page).to_have_title("Swag Labs")

    # Verify the login button is visible
    expect(page.locator("#login-button")).to_be_visible()