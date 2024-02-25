from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

new_tab_link_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[1]')
new_tab_button_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[2]')
new_tab_link_selector = (By.XPATH, '//*[@id="new-page-link"]')
new_tab_button_selector = (By.XPATH, '//*[@id="new-page-button"]')
result_string_selector = (By.XPATH, '//*[@id="result-text"]')


class TabPage(BasePage):

    def open_tab_page(self):
        return self.browser.get('https://www.qa-practice.com/elements/new_tab/link')

    def new_tab_link_tab(self):
        return self.browser.find_element(*new_tab_link_tab_selector)

    def new_tab_button_tab(self):
        return self.browser.find_element(*new_tab_button_tab_selector)

    def new_tab_link(self):
        return self.browser.find_element(*new_tab_link_selector)

    def new_tab_button(self):
        return self.browser.find_element(*new_tab_button_selector)

    def result_string(self):
        return self.browser.find_element(*result_string_selector)

    def new_tab_link_tab_click(self):
        return self.new_tab_link_tab().click()

    def new_tab_button_tab_click(self):
        return self.new_tab_button_tab().click()

    def new_tab_link_click(self):
        return self.new_tab_link().click()

    def new_tab_button_click(self):
        return self.new_tab_button().click()



