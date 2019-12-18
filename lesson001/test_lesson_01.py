#!/usr/bin/python3
# -*- encoding=utf8 -*-
"""Test of the web service ip-api.com. It checks the default parameters of the JSON version."""

import re
import csv
import pytest
import requests


@pytest.fixture(scope='session')
def result():
    """Get JSON with network parameters of the current client IP address.
     To change the response, you can use proxy servers from the comments."""

    result = requests.get('http://ip-api.com/json',
                          # proxies={"http": "47.254.69.158:9999"}
                          # proxies={"http": "43.229.72.214:52360"}
                          # proxies={"http": "114.198.135.250:3128"}
                          )
    return result


@pytest.fixture()
def zone_list():
    """Get a time zone list from the CSV file"""

    with open('lesson001/zone.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        zone_list = [row[2] for row in read_csv]
    return zone_list


@pytest.fixture()
def country_list():
    """Get a country list from the CSV file"""

    with open('lesson001/country.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        country_list = [row[1] for row in read_csv]
    return country_list


@pytest.fixture()
def country_code_list():
    """Get a country codes from the CSV file."""

    with open('lesson001/country.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        country_code_list = [row[0] for row in read_csv]
    return country_code_list


def test_status_code(result):
    """Check the status of HTTP request."""

    assert result.status_code == 200


def test_status(result):
    """Check the 'status' field."""

    assert (result.json()['status']) == 'success', \
        "Value of 'status' field is not equal 'success'."


def test_value_type(result):
    """
    Check a data type of value for the this JSON fields:
    'as', 'city', 'isp', 'org' 'region' 'regionName'
    """

    assert isinstance(result.json()['as'], str), "The value of field 'as' not a string."
    assert isinstance(result.json()['city'], str), "The value of field 'city' not a string."
    assert isinstance(result.json()['isp'], str), "The value of field 'isp' not a string."
    assert isinstance(result.json()['org'], str), "The value of field 'org' not a string."
    assert isinstance(result.json()['region'], str), "The value of field 'region' not a string."
    assert isinstance(result.json()['regionName'], str), "The value of field 'regionName' not a str"
    assert isinstance(result.json()['zip'], str), "The value of field 'zip' not a string."


def test_country_code_field(result, country_code_list):
    """Check that a value of 'countryCode' is present in the list of country codes."""

    assert result.json()['countryCode'] in country_code_list, \
        "The value of field 'countryCode' not present in the list of country codes."


def test_country_field(result, country_list):
    """Check that country list contain a value of 'country' field."""

    assert result.json()['country'] in country_list, \
        "The value of field 'country' not in the country list."


def test_timezone(result, zone_list):
    """Check that time zone list contain a value of 'timezone' field."""

    assert result.json()['timezone'] in zone_list, \
        "The value of field 'timezone' not in the timezone list."


def test_ip_adress(result):
    """Check format of a 'query' (IP-address) field by regular expression."""

    assert re.match(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)'
                    r'{3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                    result.json()['query']), \
        "The value of a 'query' field is not correct IP address."


def test_lat(result):
    """Check that a value of the 'lat' field is in a given range."""

    assert -90 <= result.json()['lat'] <= 90, \
        "Value of the 'lat' field is not in a given range."


def test_lon(result):
    """Check that a value of the 'lon' field is in a given range."""

    assert -180 <= result.json()['lon'] <= 180, \
        "Value of the 'lon' field is not in a given range."
