from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_homepage_text_input(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.text_input_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/input/simple'


def test_homepage_simple_button(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.simple_button_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/button/simple'


def test_homepage_single_checkbox(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.single_checkbox_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/checkbox/single_checkbox'


def test_homepage_text_area(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.text_area_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/textarea/single'


def test_homepage_select_input(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.select_input_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/select/single_select'


def test_homepage_homepage(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.homepage_click()
    home_page.single_ui_el_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/'


def test_homepage_contact_link(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    link = home_page.contact_link()
    home_page.actions_move_and_click(link)
    assert home_page.current_url() == 'https://www.qa-practice.com/contact/'


def test_homepage_whats_new_link(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    link = home_page.whats_new_link()
    home_page.actions_move_and_click(link)
    assert home_page.current_url() == 'https://www.qa-practice.com/whats_new/'


def test_homepage_qa_practice_link(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    link = home_page.qa_practice_link()
    home_page.actions_move_and_click(link)
    assert home_page.current_url() == 'https://www.qa-practice.com/'


def test_homepage_inputs_sub_menu(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.single_ui_el_click()
    home_page.inputs_sub_menu_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/input/simple'


def test_homepage_buttons_sub_menu(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.single_ui_el_click()
    home_page.buttons_sub_menu_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/button/simple'


def test_homepage_checkbox_sub_menu(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.single_ui_el_click()
    home_page.checkbox_sub_menu_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/checkbox/single_checkbox'


def test_homepage_select_sub_menu(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.single_ui_el_click()
    home_page.select_sub_menu_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/select/single_select'


def test_homepage_new_tab_sub_menu(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.single_ui_el_click()
    home_page.new_tab_sub_menu_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/new_tab/link'


def test_homepage_next_area_sub_menu(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.single_ui_el_click()
    home_page.next_area_sub_menu_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/textarea/single'


def test_homepage_alerts_sub_menu(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.single_ui_el_click()
    home_page.alerts_sub_menu_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/alert/alert'


def test_homepage_drag_and_drop_sub_menu(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.single_ui_el_click()
    home_page.drag_and_drop_sub_menu_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/dragndrop/boxes'


def test_homepage_iframe_sub_menu(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.single_ui_el_click()
    home_page.iframe_sub_menu_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/iframe/iframe_page'


def test_homepage_pop_up_sub_menu(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    home_page.single_ui_el_click()
    home_page.pop_up_sub_menu_click()
    assert home_page.current_url() == 'https://www.qa-practice.com/elements/popup/modal'


def test_homepage_sub_menu(browser):
    home_page = HomePage(browser)
    home_page.open_homepage()
    assert home_page.inputs_sub_menu().is_displayed() is False
    assert home_page.buttons_sub_menu().is_displayed() is False
    assert home_page.checkbox_sub_menu().is_displayed() is False
    assert home_page.select_sub_menu().is_displayed() is False
    assert home_page.new_tab_sub_menu().is_displayed() is False
    assert home_page.next_area_sub_menu().is_displayed() is False
    assert home_page.alerts_sub_menu().is_displayed() is False
    assert home_page.drag_and_drop_sub_menu().is_displayed() is False
    assert home_page.iframe_sub_menu().is_displayed() is False
    assert home_page.pop_up_sub_menu().is_displayed() is False
    home_page.single_ui_el_click()
    WebDriverWait(home_page.browser, 5).until(
        EC.visibility_of(home_page.pop_up_sub_menu())
    )
    assert home_page.inputs_sub_menu().is_displayed() is True
    assert home_page.buttons_sub_menu().is_displayed() is True
    assert home_page.checkbox_sub_menu().is_displayed() is True
    assert home_page.select_sub_menu().is_displayed() is True
    assert home_page.new_tab_sub_menu().is_displayed() is True
    assert home_page.next_area_sub_menu().is_displayed() is True
    assert home_page.alerts_sub_menu().is_displayed() is True
    assert home_page.drag_and_drop_sub_menu().is_displayed() is True
    assert home_page.iframe_sub_menu().is_displayed() is True
    assert home_page.pop_up_sub_menu().is_displayed() is True
