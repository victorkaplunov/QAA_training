#!/usr/bin/python3
# -*- encoding=utf8 -*-

import pytest
import requests
import json

"""Test of the web service ip-api.com, the test checks the default parameters of the JSON version."""


@pytest.fixture(scope='session')
def data():
    """Load examples from JSON"""
    
    with open("data.json", 'r', encoding='utf8') as file:
        filedata = file.read()
        data = json.loads(filedata)
        return data


@pytest.fixture(scope='session')
def data_negative():
    """Load examples from JSON"""
    
    with open("data_negative.json", 'r', encoding='utf8') as file:
        filedata = file.read()
        data = json.loads(filedata)
        return data


@pytest.fixture()
def result(ip_address):
    """Get response with JSON with network parameters of the current
    client IP address. Print JSON in console output"""
    
    result = requests.get('http://ip-api.com/json/' + ip_address)
    print(json.dumps(result.json(), indent=4))
    return result


@pytest.mark.parametrize("ip_address", [
    pytest.param("47.254.69.158", marks=pytest.mark.basic, id="Alibaba.com LLC"),
    pytest.param("43.229.72.214", marks=pytest.mark.basic, id='Kappa E-Ventures Private Limited'),
    pytest.param("114.198.135.250", marks=pytest.mark.basic, id='Globalreach'),
    ])
def test_ddt(result, ip_address, data):
    """Compare data from examples JSON file and result."""
    
    assert result.json() == data[ip_address]


@pytest.mark.parametrize("ip_address", [
    pytest.param("127.0.0.1", marks=pytest.mark.basic, id='Localhost'),
    pytest.param("192.168.0.1", marks=pytest.mark.basic, id='Reserved private IPv4 network ranges'),
    pytest.param("255.255.255.0", marks=pytest.mark.basic, id='Subnet mask'),
    pytest.param("169.254.0.1", marks=pytest.mark.basic, id='APIPA')
    ])
def test_ddt_negative(result, ip_address, data_negative):
    """Compare data from examples JSON file and result."""
    
    assert result.json() == data_negative[ip_address]
