from pages.iframe_page import IframePage


def test_iframe(browser):
    ip = IframePage(browser)
    ip.open_iframe_page()
    iframe = ip.iframe()
    ip.browser.switch_to.frame(iframe)
    ip.open_link(ip.homepage_link())
    assert ip.text_input_homepage().text == 'Text input'
