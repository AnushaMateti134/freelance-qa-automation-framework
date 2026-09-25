
import pytest
from playwright.sync_api import expect


import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_saucedemo_homepage_loads(page, base_url):
    page.goto(base_url)

    page.screenshot(
        path="test-results/homepage.png",
        full_page=True
    )

    expect(page).to_have_title("Swag Labs")