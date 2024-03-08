from pages.select_page import SelectPage
from utilities.random_string import random_multiple_selects
from utilities.random_string import random_programming_language


def test_select_page_single(browser):
    sp = SelectPage(browser)
    sp.open_select_page()
    language = random_programming_language()
    sp.select_by_visible_text(sp.choose_language_selects(), language)
    sp.submit_button_click()
    assert sp.result_string().text == language


def test_select_page_multiple(browser):
    sp = SelectPage(browser)
    sp.open_select_page()
    sp.multiple_selects_tab_click()
    multiple = random_multiple_selects()
    sp.send_keys(sp.place_selects(), multiple[0])
    sp.send_keys(sp.transport_selects(), multiple[1])
    sp.send_keys(sp.time_selects(), multiple[2])
    sp.submit_button_click()
    assert sp.result_string().text == f'to go by {multiple[1]} to the {multiple[0]} {multiple[2]}'.lower()
