#!/usr/bin/python3
# -*- encoding=utf8 -*-

"""Test of web service ip-api.com. Example of fuzzy testing and using
JSON schema. This test checks the default parameters of the JSON version."""

import pytest
import requests


# String with all punctuation symbols
SYMBOLS_STRING = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
# Convert it to list
i = iter(SYMBOLS_STRING)
SYMBOL_LIST = [(next(i)) for e in range(len(SYMBOLS_STRING))]


@pytest.fixture(params=SYMBOL_LIST)
def symbol_params():
    """Create parametrized fixture for test_incorrect_symbol.
    Parameter is the list of punctuation symbols."""
    return iter(SYMBOL_LIST)


@pytest.mark.parametrize("symbol_params", symbol_params())
def test_incorrect_symbol(symbol_params):
    """Repeat request ip-api.com with incorrect symbol end check response."""

    response = requests.get('http://ip-api.com/json/' + symbol_params)
    print(response.text)
    assert response.status_code == 200
