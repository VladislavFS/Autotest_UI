from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

text_input_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[1]')
email_field_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[2]')
password_field_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[3]')
text_string_selector = (By.XPATH, '//*[@id="id_text_string"]')
result_string_selector = (By.XPATH, '//*[@id="result-text"]')
text_string_error_selector = (By.XPATH, '//*[@id="error_1_id_text_string"]/strong')
email_string_selector = (By.XPATH, '//*[@id="id_email"]')
email_string_error_selector = (By.XPATH, '//*[@id="error_1_id_email"]/strong')
password_string_selector = (By.XPATH, '//*[@id="id_password"]')
password_string_error_selector = (By.XPATH, '//*[@id="error_1_id_password"]/strong')


class InputPage(BasePage):

    def open_input_page(self):
        return self.browser.get('https://www.qa-practice.com/elements/input/simple')

    def text_input_tab(self):
        return self.browser.find_element(*text_input_tab_selector)

    def email_field_tab(self):
        return self.browser.find_element(*email_field_tab_selector)

    def password_field_tab(self):
        return self.browser.find_element(*password_field_tab_selector)

    def text_string(self):
        return self.browser.find_element(*text_string_selector)

    def result_string(self):
        return self.browser.find_element(*result_string_selector)

    def text_string_error(self):
        return self.browser.find_element(*text_string_error_selector)

    def email_string(self):
        return self.browser.find_element(*email_string_selector)

    def email_string_error(self):
        return self.browser.find_element(*email_string_error_selector)

    def password_string(self):
        return self.browser.find_element(*password_string_selector)

    def password_string_error(self):
        return self.browser.find_element(*password_string_error_selector)

    def text_input_tab_click(self):
        return self.text_input_tab().click()

    def email_field_tab_click(self):
        return self.email_field_tab().click()

    def password_field_tab_click(self):
        return self.password_field_tab().click()
