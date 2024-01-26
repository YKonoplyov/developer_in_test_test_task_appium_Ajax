import os
import logging
from contextlib import nullcontext as does_not_raise

import pytest
from dotenv import load_dotenv
from selenium.common.exceptions import TimeoutException

load_dotenv()

LOGIN_EMAIL = "qa.ajax.app.automation@gmail.com"
VALID_PASSWORD = os.getenv("VALID_PASSWORD")
VALIDATION_ERROR_MESSAGE = "Invalid Login or Password"


@pytest.mark.parametrize(
    "login,password,expectation",
    [
        (LOGIN_EMAIL, VALID_PASSWORD, does_not_raise()),
        # (LOGIN_EMAIL, "123456789", pytest.raises(TimeoutException)),
        # ("zynoviy_pupka@faynanet.com", "123456789", pytest.raises(TimeoutException))
    ],
    ids=[
        "Valid email and password",
        # "Invalid password, valid email",
        # "Invalid email and password"
    ],
)
def test_user_login(user_login_fixture, login: str, password: str, expectation):
    print(pytest.Item.name)
    logging.info(f"Running test case: {login}")
    user_login_fixture.log_in(login=login, password=password)
    with expectation:
        assert (
            user_login_fixture.find_element_by_id(element_id="menuDrawer") is not None
        )
    logging.info(f"Finished test case: {login}")
