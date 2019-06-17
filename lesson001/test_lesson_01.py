#!/usr/bin/python3
# -*- encoding=utf8 -*-


import pytest
import requests
import re
import csv
"""Тест англоязычной JSON-версии web-сервиса ip-api.com, в тесте проводится проверка параметров по-умолчанию."""

@pytest.fixture(scope='session')
def result():
    """Получение JSON с сетевыми параметрами текущего IP-адреса клиента.
    Для измененеия ответа можно использовать прокси серверы из комментариев"""
    result = requests.get('http://ip-api.com/json',
                          # proxies={"http": "47.254.69.158:9999"}
                          # proxies={"http": "43.229.72.214:52360"}
                          # proxies={"http": "114.198.135.250:3128"}
                          )
    # print(result.text)
    return result


@pytest.fixture()
def zone_list():
    """Получаем список временных зон из CSV-файла"""
    with open('zone.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        zone_list = [row[2] for row in read_csv]
    return zone_list


@pytest.fixture()
def country_list():
    """Получаем список кодов стран и список названий стран из CSV-файла"""
    with open('country.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        country_list = [row[1] for row in read_csv]
        # print(country_list)
    return country_list


@pytest.fixture()
def country_code_list():
    """Получаем список кодов стран и список названий стран из CSV-файла"""
    with open('country.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        country_code_list = [row[0] for row in read_csv]
        # print(country_code_list)
    return country_code_list


def test_status_code(result, zone_list):
    """Статус код HTTP запроса: 200"""
    assert result.status_code == 200


def test_status(result):
    """Значение поля status имеет значение success"""
    assert (result.json()['status']) == 'success', "Значение поля status не равно строке 'success'"


def test_value_type(result):
    """Проверка типов данных для полей JSON"""
    assert type(result.json()['as']) is str, "Содержимое поля 'as' не строка"
    assert type(result.json()['city']) is str, "Содержимое поля 'city' не строка"
    assert type(result.json()['isp']) is str, "Содержимое поля 'isp' не строка"
    assert type(result.json()['org']) is str, "Содержимое поля 'org' не строка"
    assert type(result.json()['region']) is str, "Содержимое поля 'region' не строка"
    assert type(result.json()['regionName']) is str, "Содержимое поля 'regionName' не строка"
    assert type(result.json()['zip']) is str, "Содержимое поля 'zip' не строка"


def test_country_code_field(result, country_code_list):
    """Значение поля countryCode входит в эталонный список кодов стран"""
    assert (result.json()['countryCode']) in country_code_list, "Значение поля countryCode не входит в список кодов"


def test_country_field(result, country_list):
    """Значение поля timezone входит в эталонный список временных зон"""
    assert (result.json()['country']) in country_list, "Значение поля country не входит в список стран"


def test_timezone(result, zone_list):
    """Значение поля timezone входит в эталонный список временных зон"""
    assert (result.json()['timezone']) in zone_list, "Значение поля timezone не входит в список временных зон"


def test_ip_adress(result):
    """Значение поля query (IP-address) имеет допустимое значение"""
    assert re.match(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                    result.json()['query']), "Содержимое поля IP-адреса не соответствует шаблону"


def test_lat(result):
    """Значение широты входит в допустимый диапазон"""
    assert -90 <= result.json()['lat'] <= 90, "Значение поля lat не соответсвуюет диапазону допустимых значений"


def test_lon(result):
    """Значение долготы входит в допустимый диапазон"""
    assert -180 <= result.json()['lon'] <= 180, "Значение поля lon не соответсвуюет диапазону допустимых значений"
