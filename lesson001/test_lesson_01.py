#!/usr/bin/python3
# -*- encoding=utf8 -*-


import pytest
import requests
import re
import csv
"""Test of the web service ip-api.com, the test checks the default parameters of the JSON version."""


@pytest.fixture(scope='session')
def result():
    """Get JSON with network parameters of the current client IP address.
     To change the response, you can use proxy servers from the comments."""
    result = requests.get('http://ip-api.com/json',
                          # proxies={"http": "47.254.69.158:9999"}
                          # proxies={"http": "43.229.72.214:52360"}
                          # proxies={"http": "114.198.135.250:3128"}
                          )
    # print(json.dumps(result.json(), indent=4, sort_keys=True))
    return result


@pytest.fixture()
def zone_list():
    """Get a time zone list from the CSV file"""
    with open('zone.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        zone_list = [row[2] for row in read_csv]
    return zone_list


@pytest.fixture()
def country_list():
    """Get a country list the CSV file"""
    with open('country.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        country_list = [row[1] for row in read_csv]
        # print(country_list)
    return country_list


@pytest.fixture()
def country_code_list():
    """Get a country codes the CSV file."""
    with open('country.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        country_code_list = [row[0] for row in read_csv]
        # print(country_code_list)
    return country_code_list


def test_status_code(result, zone_list):
    """Check the status of HTTP request."""
    assert result.status_code == 200


def test_status(result):
    """Check the 'status' field."""
    assert (result.json()['status']) == 'success',\
        "Value of 'status' field is not equal 'success'."


def test_value_type(result):
    """
    Check a data type of value for the this JSON fields:
    'as', 'city', 'isp', 'org' 'region' 'regionName' """
    assert type(result.json()['as']) is str,\
        "The value of field 'as' not a string."
    assert type(result.json()['city']) is str,\
        "The value of field 'city' not a string."
    assert type(result.json()['isp']) is str,\
        "The value of field 'isp' not a string."
    assert type(result.json()['org']) is str,\
        "The value of field 'org' not a string."
    assert type(result.json()['region']) is str,\
        "The value of field 'region' not a string."
    assert type(result.json()['regionName']) is str,\
        "The value of field 'regionName' not a string."
    assert type(result.json()['zip']) is str,\
        "The value of field 'zip' not a string."


def test_country_code_field(result, country_code_list):
    """Check that a value of 'countryCode' in the country code list."""
    assert (result.json()['countryCode']) in country_code_list,\
        "The value of field 'countryCode' not in the country code list."


def test_country_field(result, country_list):
    """Check that country list contain a value of 'countryCode' field."""
    assert (result.json()['country']) in country_list,\
        "The value of field 'countryCode' not in the country list."


def test_timezone(result, zone_list):
    """Check that time zone list contain a value of 'timezone' field."""
    assert (result.json()['timezone']) in zone_list,\
        "The value of field 'timezone' not in the timezone list."


def test_ip_adress(result):
    """Check format of a 'query' (IP-address) field/"""
    assert re.match(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)'
                    r'{3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                    result.json()['query']),\
        "The value of a 'query' field is not correct IP address."


def test_lat(result):
    """Check that a value of the 'lat' field is in a given range."""
    assert -90 <= result.json()['lat'] <= 90,\
        "Value of the 'lat' field is in a given range."


def test_lon(result):
    """Check that a value of the 'lon' field is in a given range."""
    assert -180 <= result.json()['lon'] <= 180,\
        "Value of the 'lon' field is in a given range."
