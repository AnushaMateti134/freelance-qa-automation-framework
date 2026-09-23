import pytest

from pages.login_page import LoginPage
from test_data.login_data import INVALID_USERS


@pytest.mark.parametrize(
    "username,password",
    INVALID_USERS
)
def test_invalid_login(
    page,
    base_url,
    username,
    password
):
    login_page = LoginPage(page)

    login_page.open(base_url)

    login_page.login(username, password)

    assert login_page.get_error_message() is not None