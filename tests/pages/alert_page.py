from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

alert_box_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[1]')
confirmation_box_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[2]')
prompt_box_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[3]')
click_button_selector = (By.XPATH, '//*[@id="content"]/a[1]')
result_string_selector = (By.XPATH, '//*[@id="result-text"]')


class AlertPage(BasePage):

    def open_alert_page(self):
        return self.browser.get('https://www.qa-practice.com/elements/alert/alert')

    def alert_box_tab(self):
        return self.browser.find_element(*alert_box_tab_selector)

    def confirmation_box_tab(self):
        return self.browser.find_element(*confirmation_box_tab_selector)

    def prompt_box_tab(self):
        return self.browser.find_element(*prompt_box_tab_selector)

    def click_button(self):
        return self.browser.find_element(*click_button_selector)

    def result_string(self):
        return self.browser.find_element(*result_string_selector)

    def alert_box_tab_click(self):
        return self.alert_box_tab().click()

    def confirmation_box_tab_click(self):
        return self.confirmation_box_tab().click()

    def prompt_box_tab_click(self):
        return self.prompt_box_tab().click()

    def click_button_click(self):
        return self.click_button().click()

    def focus_alert(self):
        return self.browser.switch_to.alert

    def alert_accept(self):
        alert = self.focus_alert()
        return alert.accept()

    def alert_dismiss(self):
        alert = self.focus_alert()
        return alert.dismiss()

    def alert_send_keys(self, keys):
        alert = self.focus_alert()
        return alert.send_keys(keys)





