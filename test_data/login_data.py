STANDARD_USER = "standard_user"

PASSWORD = "secret_sauce"

LOCKED_OUT_USER = "locked_out_user"

INVALID_USERS = [
    ("wrong_user", "secret_sauce"),
    ("standard_user", "wrong_password"),
    ("wrong_user", "wrong_password"),
]