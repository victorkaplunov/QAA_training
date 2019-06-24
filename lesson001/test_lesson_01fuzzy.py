#!/usr/bin/python3
# -*- encoding=utf8 -*-
# pylint: disable=redefined-outer-name
# pylint: disable=no-member

"""Test of web service ip-api.com. Example of fuzzy testing and using
JSON schema. This test checks the default parameters of the JSON version."""

import json
import pytest
import requests
from faker import Faker
from faker.providers import internet
import jsonschema


@pytest.fixture(params=list(range(5)))
def ip_address():
    """Create random IP addresses."""

    fake = Faker()
    fake.add_provider(internet)
    return iter([fake.ipv4_public()])


def test_1(ip_address):
    """Repeat request ip-api.com with random IP address end check JSON
    from response with given JSON schema."""

    with open('json_schema.json', 'r', encoding='utf8') as file:
        file_data = file.read()

    response = requests.get('http://ip-api.com/json/' + next(ip_address))
    print(json.dumps(response.json(), indent=4))
    assert jsonschema.validate(response.json(), json.loads(file_data)) is None
