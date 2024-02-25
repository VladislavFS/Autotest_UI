from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

simple_button_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[1]')
looks_like_a_button_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[2]')
disabled_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[3]')
click_button_selector = (By.XPATH, '//*[@id="submit-id-submit"]')
looks_like_a_button_selector = (By.XPATH, '//*[@id="button-form"]/a')
select_state_selector = (By.XPATH, '//*[@id="id_select_state"]')
submit_selector = (By.XPATH, '//*[@id="submit-id-submit"]')
result_string_selector = (By.XPATH, '//*[@id="result-text"]')


class ButtonsPage(BasePage):

    def open_buttons_page(self):
        return self.browser.get('https://www.qa-practice.com/elements/button/simple')

    def simple_button_tab(self):
        return self.browser.find_element(*simple_button_tab_selector)

    def looks_like_a_button_tab(self):
        return self.browser.find_element(*looks_like_a_button_tab_selector)

    def disabled_tab(self):
        return self.browser.find_element(*disabled_tab_selector)

    def click_button(self):
        return self.browser.find_element(*click_button_selector)

    def looks_like_a_button(self):
        return self.browser.find_element(*looks_like_a_button_selector)

    def select_state(self):
        return self.browser.find_element(*select_state_selector)

    def submit(self):
        return self.browser.find_element(*submit_selector)

    def result_string(self):
        return self.browser.find_element(*result_string_selector)

    def simple_button_tab_click(self):
        return self.simple_button_tab().click()

    def looks_like_a_button_tab_click(self):
        return self.looks_like_a_button_tab().click()

    def disabled_tab_click(self):
        return self.disabled_tab().click()

    def click_button_click(self):
        return self.click_button().click()

    def looks_like_a_button_click(self):
        return self.looks_like_a_button().click()

    def submit_click(self):
        return self.submit().click()
