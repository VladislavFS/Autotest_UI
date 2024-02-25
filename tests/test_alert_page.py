from tests.pages.alert_page import AlertPage
from utilities.random_string import generate_random_text_string


def test_alert_page_alert_box(browser):
    ap = AlertPage(browser)
    ap.open_alert_page()
    ap.click_button_click()
    ap.alert_accept()


def test_alert_page_confirmation_box(browser):
    ap = AlertPage(browser)
    ap.open_alert_page()
    ap.confirmation_box_tab_click()
    ap.click_button_click()
    ap.alert_accept()
    assert ap.result_string().text == 'Ok'


def test_alert_page_prompt_box(browser):
    ap = AlertPage(browser)
    ap.open_alert_page()
    ap.prompt_box_tab_click()
    ap.click_button_click()
    string = generate_random_text_string(10)
    ap.alert_send_keys(string)
    ap.alert_accept()
    assert ap.result_string().text == string
