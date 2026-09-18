
import pytest
from playwright.sync_api import Page, expect

from config.settings import BASE_URL, STANDARD_USER, PASSWORD
from pages.login_page import LoginPage


def test_login_page_loads(page: Page):
    login_page = LoginPage(page)

    login_page.open(BASE_URL)

    expect(page).to_have_title("Swag Labs")
    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()


def test_valid_login(page: Page):
    login_page = LoginPage(page)

    login_page.open(BASE_URL)
    login_page.login(STANDARD_USER, PASSWORD)

    expect(page).to_have_url(BASE_URL + "inventory.html")
    expect(page.get_by_text("Products", exact=True)).to_be_visible()


def test_login_with_empty_username(page: Page):
    login_page = LoginPage(page)

    login_page.open(BASE_URL)
    login_page.enter_password(PASSWORD)
    login_page.click_login()

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Username is required"
    )


def test_login_with_empty_password(page: Page):
    login_page = LoginPage(page)

    login_page.open(BASE_URL)
    login_page.enter_username(STANDARD_USER)
    login_page.click_login()

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Password is required"
    )


@pytest.mark.parametrize(
    "username, password",
    [
        ("standard_user", "wrong_password"),
        ("wrong_user", PASSWORD),
        ("wrong_user", "wrong_password"),
    ],
)
def test_invalid_login(
    page: Page,
    username: str,
    password: str,
):
    login_page = LoginPage(page)

    login_page.open(BASE_URL)
    login_page.login(username, password)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Username and password do not match"
    )


def test_locked_out_user(page: Page):
    login_page = LoginPage(page)

    login_page.open(BASE_URL)
    login_page.login("locked_out_user", PASSWORD)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "locked out"
    )
    