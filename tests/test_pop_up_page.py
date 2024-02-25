from pages.pop_up_page import PopUpPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_pop_up_modal(browser):
    pp = PopUpPage(browser)
    pp.open_pop_up_page()
    pp.launch_pop_up_click()
    pp.select_me_or_not_click()
    pp.send_button_click()
    assert pp.result_string().text == 'select me or not'


def test_pop_up_iframe(browser):
    pp = PopUpPage(browser)
    pp.open_pop_up_page()
    pp.iframe_pop_up_tab_click()
    pp.launch_pop_up_click()
    iframe = pp.iframe()
    pp.browser.switch_to.frame(iframe)
    WebDriverWait(pp.browser, 5).until(
        EC.visibility_of(pp.text_to_copy())
    )
    text = pp.text_to_copy().text
    pp.browser.switch_to.default_content()
    pp.check_button_click()
    pp.send_keys(pp.text_from_iframe(), text)
    assert pp.result_check_text().text == 'Correct!'
