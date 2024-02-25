from pages.input_page import InputPage
from utilities.random_string import generate_random_text_string
import pytest


@pytest.mark.parametrize('length', [2, 25])
def test_input_page_text_string(length, browser):
    input_page = InputPage(browser)
    input_page.open_input_page()
    string = generate_random_text_string(length)
    input_page.send_keys(input_page.text_string(), string)
    result = input_page.result_string().text
    assert string == result


@pytest.mark.parametrize('length,error', [
    ((1, 'ENG'), 'Please enter 2 or more characters'),
    ((26, 'ENG'), 'Please enter no more than 25 characters'),
    ((2, 'RU'), 'Enter a valid string consisting of letters, numbers, underscores or hyphens.')])
def test_input_page_text_string_error(length, error, browser):
    input_page = InputPage(browser)
    input_page.open_input_page()
    string = generate_random_text_string(*length)
    input_page.send_keys(input_page.text_string(), string)
    result = input_page.text_string_error().text
    assert error == result

# Можно добавить тесты на вкладки Email и Password, отличие будет только в плане заполенения полей
