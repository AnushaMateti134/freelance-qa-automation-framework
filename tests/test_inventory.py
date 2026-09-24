import pytest

from test_data.product_data import PRODUCTS


@pytest.mark.parametrize(
    "product_name",
    PRODUCTS
)
def test_product_can_be_added_to_cart(
    logged_in_inventory,
    product_name
):

    logged_in_inventory.add_product_to_cart(
        product_name
    )

    assert (
        logged_in_inventory.get_cart_count()
        == 1
    )
    import pytest

from test_data.product_data import PRODUCTS


@pytest.mark.regression
@pytest.mark.parametrize("product_name", PRODUCTS)
def test_product_can_be_added_to_cart(
    logged_in_inventory,
    product_name
):
    logged_in_inventory.add_product_to_cart(product_name)
    assert logged_in_inventory.get_cart_count() == 1