import logging
from contextlib import nullcontext as does_not_raise

import pytest
from tests.login.test_login import LOGIN_EMAIL, VALID_PASSWORD


@pytest.mark.parametrize(
    "menu_element_id,target_element_text,expectation",
    [
        ("settings", "Sign Out", does_not_raise()),
        ("help", "CombiProtect", does_not_raise()),
        ("logs", "Delete", does_not_raise()),
    ],
)
def test_side_menu(
    user_login_fixture, menu_element_id: str, target_element_text: str, expectation
):
    logging.info(f'Test Side Menu started for menu element "{menu_element_id}"')
    user_login_fixture.log_in(LOGIN_EMAIL, VALID_PASSWORD)
    user_login_fixture.open_sidebar()
    menu_element = user_login_fixture.find_element_by_id(menu_element_id)
    user_login_fixture.click_element(menu_element)
    with expectation:
        assert user_login_fixture.find_element_by_text(target_element_text) is not None
    logging.info(f'Test Side Menu completed for menu element "{menu_element_id}"')
