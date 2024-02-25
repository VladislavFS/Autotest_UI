from pages.new_tab_page import TabPage


def test_new_tab_link(browser):
    tp = TabPage(browser)
    tp.open_tab_page()
    tp.new_tab_link_click()
    tp.focus_new_tab()
    assert tp.current_url() == 'https://www.qa-practice.com/elements/new_tab/new_page'
    assert tp.result_string().text == 'I am a new page in a new tab'


def test_new_tab_button(browser):
    tp = TabPage(browser)
    tp.open_tab_page()
    tp.new_tab_button_tab_click()
    tp.new_tab_button_click()
    tp.focus_new_tab()
    assert tp.current_url() == 'https://www.qa-practice.com/elements/new_tab/new_page'
    assert tp.result_string().text == 'I am a new page in a new tab'
