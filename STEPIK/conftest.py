"""Utilities for tests"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """
    CLI parameter for test.
    Парметр вызова теста из командной строки.
    """
    parser.addoption('--language', action='store', default='ru',
                     help="Choose accept_languages HTTP request header value "
                          "for browser. Accept any ISO-639 language codes.")


@pytest.fixture()
def browser(request):
    """
    The fixture for calling browser with given parameters.
    Фикстура вызова браузера с заданными параметрами
    """
    user_language = request.config.getoption("language")
    print(user_language)
    options = Options()
    options.add_experimental_option('prefs',
                                    {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    return browser
