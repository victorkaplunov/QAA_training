"""
This test check a presence of "Add to basket" button on book shop site .
You can use --language=xx parameter at running this test, when "xx" is
a ISO-639 language cod.

Тест проверяет, что страница товара на сайте интернет магазина
содержит кнопку добавления товара в корзину.
При запуске теста можно использовать параметр --language=xx, в котором задается
заголовок HTTP запроса "accept-language" (предпочитаемый язык), где "xx" - код
языка по ISO-639.
"""
import time

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    """Check "Add to basket" button"""
    browser.get(LINK)
    time.sleep(5)
    assert browser.find_element_by_css_selector('#add_to_basket_form button').is_displayed(),\
        'The "Add to basket" button is not displayed.'
