from pages.checkbox_page import CheckboxPage
import pytest


def test_checkbox_page_single(browser):
    cp = CheckboxPage(browser)
    cp.open_checkbox_page()
    cp.select_me_or_not_checkbox_click()
    cp.submit_button_click()
    result = cp.result_string().text
    assert result == 'select me or not'


@pytest.mark.parametrize('checkbox1', ['one_checkbox_click()'])
@pytest.mark.parametrize('checkbox2, result',
                         [('two_checkbox_click()', 'one, two'),
                          ('three_checkbox_click()', 'one, three')])
def test_checkbox_page_checkboxes(checkbox1, checkbox2, result, browser):
    cp = CheckboxPage(browser)
    cp.open_checkbox_page()
    cp.checkboxes_tab_click()
    eval(f'cp.{checkbox1}')
    eval(f'cp.{checkbox2}')
    cp.submit_button_click()
    result_text = cp.result_string().text
    assert result_text == result
