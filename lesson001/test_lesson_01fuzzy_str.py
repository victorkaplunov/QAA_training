#!/usr/bin/python3
# -*- encoding=utf8 -*-

"""Test of web service ip-api.com. Example of fuzzy testing and using
JSON schema. This test checks the default parameters of the JSON version."""

import pytest
import requests


# List with all punctuation symbols
SYMBOL_LIST = list(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")


@pytest.fixture(params=SYMBOL_LIST)
def symbol_params():
    """Create parametrized fixture for test_incorrect_symbol."""

    return iter(SYMBOL_LIST)


@pytest.mark.parametrize("symbol_params", SYMBOL_LIST)
def test_incorrect_symbol(symbol_params):
    """Repeat request ip-api.com with incorrect symbol end check response."""

    response = requests.get('http://ip-api.com/json/' + symbol_params)
    print(response.text)
    assert response.status_code == 200
