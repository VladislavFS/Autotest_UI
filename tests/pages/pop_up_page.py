from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

modal_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[1]')
iframe_pop_up_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[2]')
launch_pop_up_selector = (By.XPATH, '//*[@id="content"]/button')
select_me_or_not_selector = (By.XPATH, '//*[@id="id_checkbox_0"]')
send_button_selector = (By.XPATH, '//*[@id="exampleModal"]/div/div/div[3]/button[2]')
iframe_selector = (By.XPATH, '//*[@id="exampleModal"]/div/div/div/iframe')
text_to_copy_selector = (By.XPATH, '//*[@id="text-to-copy"]')
check_button_selector = (By.XPATH, '//*[@id="exampleModal"]/div/div/div/div[2]/button[2]')
text_from_iframe_selector = (By.XPATH, '//*[@id="id_text_from_iframe"]')
submit_button_selector = (By.XPATH, '//*[@id="submit-id-submit"]')
result_check_text_selector = (By.XPATH, '//*[@id="check-result"]')
result_string_selector = (By.XPATH, '//*[@id="result-text"]')


class PopUpPage(BasePage):

    def open_pop_up_page(self):
        return self.browser.get('https://www.qa-practice.com/elements/popup/modal')

    def modal_tab(self):
        return self.browser.find_element(*modal_tab_selector)

    def iframe_pop_up_tab(self):
        return self.browser.find_element(*iframe_pop_up_tab_selector)

    def launch_pop_up(self):
        return self.browser.find_element(*launch_pop_up_selector)

    def select_me_or_not(self):
        return self.browser.find_element(*select_me_or_not_selector)

    def send_button(self):
        return self.browser.find_element(*send_button_selector)

    def iframe(self):
        return self.browser.find_element(*iframe_selector)

    def text_to_copy(self):
        return self.browser.find_element(*text_to_copy_selector)

    def check_button(self):
        return self.browser.find_element(*check_button_selector)

    def text_from_iframe(self):
        return self.browser.find_element(*text_from_iframe_selector)

    def submit_button(self):
        return self.browser.find_element(*submit_button_selector)

    def result_check_text(self):
        return self.browser.find_element(*result_check_text_selector)

    def result_string(self):
        return self.browser.find_element(*result_string_selector)

    def modal_tab_click(self):
        return self.modal_tab().click()

    def iframe_pop_up_tab_click(self):
        return self.iframe_pop_up_tab().click()

    def launch_pop_up_click(self):
        return self.launch_pop_up().click()

    def select_me_or_not_click(self):
        return self.select_me_or_not().click()

    def send_button_click(self):
        return self.send_button().click()

    def check_button_click(self):
        return self.check_button().click()

    def submit_button_click(self):
        return self.submit_button().click()

