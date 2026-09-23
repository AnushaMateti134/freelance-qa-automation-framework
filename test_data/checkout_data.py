CHECKOUT_USERS = [
    (
        "Anusha",
        "Mateti",
        "12345"
    ),
    (
        "John",
        "Smith",
        "560001"
    ),
    (
        "Test",
        "User",
        "110001"
    ),
]


INVALID_CHECKOUT_DATA = [
    ("", "Mateti", "12345", "Error: First Name is required"),
    ("Anusha", "", "12345", "Error: Last Name is required"),
    ("Anusha", "Mateti", "", "Error: Postal Code is required"),
]