from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

single_checkbox_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[1]')
checkboxes_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[2]')
select_me_or_not_checkbox_selector = (By.XPATH, '//*[@id="id_checkbox_0"]')
one_checkbox_selector = (By.XPATH, '//*[@id="id_checkboxes_0"]')
two_checkbox_selector = (By.XPATH, '//*[@id="id_checkboxes_1"]')
three_checkbox_selector = (By.XPATH, '//*[@id="id_checkboxes_2"]')
submit_button_selector = (By.XPATH, '//*[@id="submit-id-submit"]')
result_string_selector = (By.XPATH, '//*[@id="result-text"]')


class CheckboxPage(BasePage):

    def open_checkbox_page(self):
        return self.browser.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')

    def single_checkbox_tab(self):
        return self.browser.find_element(*single_checkbox_tab_selector)

    def checkboxes_tab(self):
        return self.browser.find_element(*checkboxes_tab_selector)

    def select_me_or_not_checkbox(self):
        return self.browser.find_element(*select_me_or_not_checkbox_selector)

    def one_checkbox(self):
        return self.browser.find_element(*one_checkbox_selector)

    def two_checkbox(self):
        return self.browser.find_element(*two_checkbox_selector)

    def three_checkbox(self):
        return self.browser.find_element(*three_checkbox_selector)

    def submit_button(self):
        return self.browser.find_element(*submit_button_selector)

    def result_string(self):
        return self.browser.find_element(*result_string_selector)

    def single_checkbox_tab_click(self):
        return self.single_checkbox_tab().click()

    def checkboxes_tab_click(self):
        return self.checkboxes_tab().click()

    def select_me_or_not_checkbox_click(self):
        return self.select_me_or_not_checkbox().click()

    def one_checkbox_click(self):
        return self.one_checkbox().click()

    def two_checkbox_click(self):
        return self.two_checkbox().click()

    def three_checkbox_click(self):
        return self.three_checkbox().click()

    def submit_button_click(self):
        return self.submit_button().click()
