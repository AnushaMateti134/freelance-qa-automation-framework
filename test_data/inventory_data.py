from playwright.sync_api import expect

from config.settings import BASE_URL, STANDARD_USER, PASSWORD
from pages.login_page import LoginPage


def test_valid_login(login_page: LoginPage):
    login_page.open(BASE_URL)
    login_page.login(STANDARD_USER, PASSWORD)

    expect(login_page.page).to_have_url(
        BASE_URL + "inventory.html"
    )
    expect(
        login_page.page.get_by_text("Products", exact=True)
    ).to_be_visible()