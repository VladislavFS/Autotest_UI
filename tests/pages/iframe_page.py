from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

iframe_selector = (By.XPATH, '//*[@id="content"]/iframe')
homepage_link_selector = (By.XPATH, '/html/body/div/footer/div/p[3]/a[1]')
text_input_homepage_selector = (By.XPATH, '//*[@id="content"]/div/ol/li[1]/a')


class IframePage(BasePage):

    def open_iframe_page(self):
        return self.browser.get('https://www.qa-practice.com/elements/iframe/iframe_page')

    def iframe(self):
        return self.browser.find_element(*iframe_selector)

    def homepage_link(self):
        return self.browser.find_element(*homepage_link_selector)

    def text_input_homepage(self):
        return self.browser.find_element(*text_input_homepage_selector)
