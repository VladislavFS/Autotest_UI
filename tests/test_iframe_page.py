from pages.iframe_page import IframePage


def test_iframe(browser):
    ip = IframePage(browser)
    ip.open_iframe_page()
    iframe = ip.iframe()
    ip.browser.switch_to.frame(iframe)
    ip.actions_move_and_click(ip.homepage_link())
    assert ip.text_input_homepage().text == 'Text input'
