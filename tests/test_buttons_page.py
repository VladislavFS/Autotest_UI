from pages.buttons_page import ButtonsPage


def test_buttons_page_simple_button(browser):
    buttons_page = ButtonsPage(browser)
    buttons_page.open_buttons_page()
    buttons_page.click_button_click()
    assert buttons_page.result_string().text == 'Submitted'


def test_buttons_page_like_a_button(browser):
    buttons_page = ButtonsPage(browser)
    buttons_page.open_buttons_page()
    buttons_page.looks_like_a_button_tab_click()
    buttons_page.looks_like_a_button_click()
    assert buttons_page.result_string().text == 'Submitted'


def test_buttons_page_disabled(browser):
    buttons_page = ButtonsPage(browser)
    buttons_page.open_buttons_page()
    buttons_page.disabled_tab_click()
    buttons_page.send_keys(buttons_page.select_state(), 'Enabled')
    buttons_page.submit_click()
    assert buttons_page.result_string().text == 'Submitted'
