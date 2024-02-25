from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

single_select_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[1]')
multiple_selects_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[2]')
choose_language_selects_selector = (By.XPATH, '//*[@id="id_choose_language"]')
place_selects_selector = (By.XPATH, '//*[@id="id_choose_the_place_you_want_to_go"]')
transport_selects_selector = (By.XPATH, '//*[@id="id_choose_how_you_want_to_get_there"]')
time_selects_selector = (By.XPATH, '//*[@id="id_choose_when_you_want_to_go"]')
submit_button_selector = (By.XPATH, '//*[@id="submit-id-submit"]')
result_string_selector = (By.XPATH, '//*[@id="result-text"]')


class SelectPage(BasePage):

    def open_select_page(self):
        return self.browser.get('https://www.qa-practice.com/elements/select/single_select')

    def single_select_tab(self):
        return self.browser.find_element(*single_select_tab_selector)

    def multiple_selects_tab(self):
        return self.browser.find_element(*multiple_selects_tab_selector)

    def choose_language_selects(self):
        return self.browser.find_element(*choose_language_selects_selector)

    def place_selects(self):
        return self.browser.find_element(*place_selects_selector)

    def transport_selects(self):
        return self.browser.find_element(*transport_selects_selector)

    def time_selects(self):
        return self.browser.find_element(*time_selects_selector)

    def submit_button(self):
        return self.browser.find_element(*submit_button_selector)

    def result_string(self):
        return self.browser.find_element(*result_string_selector)

    def single_select_tab_click(self):
        return self.single_select_tab().click()

    def multiple_selects_tab_click(self):
        return self.multiple_selects_tab().click()

    def submit_button_click(self):
        return self.submit_button().click()
