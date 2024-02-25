from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

text_input_selector = (By.XPATH, '//*[@id="content"]/div/ol/li[1]')
simple_button_selector = (By.XPATH, '//*[@id="content"]/div/ol/li[2]')
single_checkbox_selector = (By.XPATH, '//*[@id="content"]/div/ol/li[3]')
text_area_selector = (By.XPATH, '//*[@id="content"]/div/ol/li[4]')
select_input_selector = (By.XPATH, '//*[@id="content"]/div/ol/li[5]')
homepage_selector = (By.XPATH, '//*[@id="sidebar"]/div/ul/li[1]')
single_ui_el_selector = (By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]')
inputs_sub_menu_selector = (By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[1]')
buttons_sub_menu_selector = (By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[2]')
checkbox_sub_menu_selector = (By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[3]')
select_sub_menu_selector = (By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[4]')
new_tab_sub_menu_selector = (By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[5]')
next_area_sub_menu_selector = (By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[6]')
alerts_sub_menu_selector = (By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[7]')
drag_and_drop_sub_menu_selector = (By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[8]')
iframe_sub_menu_selector = (By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[9]')
pop_up_sub_menu_selector = (By.XPATH, '//*[@id="sidebar"]/div/ul/li[2]/ul/li[10]')
contact_link_selector = (By.XPATH, '/html/body/div[3]/a[1]')
whats_new_link_selector = (By.XPATH, '/html/body/div[3]/a[2]')
qa_practice_link_selector = (By.XPATH, '/html/body/footer/div/a')


class HomePage(BasePage):

    def open_homepage(self):
        return self.browser.get('https://www.qa-practice.com/')

    def homepage(self):
        return self.browser.find_element(*homepage_selector)

    def text_input(self):
        return self.browser.find_element(*text_input_selector)

    def simple_button(self):
        return self.browser.find_element(*simple_button_selector)

    def single_checkbox(self):
        return self.browser.find_element(*single_checkbox_selector)

    def text_area(self):
        return self.browser.find_element(*text_area_selector)

    def select_input(self):
        return self.browser.find_element(*select_input_selector)

    def single_ui_el(self):
        return self.browser.find_element(*single_ui_el_selector)

    def inputs_sub_menu(self):
        return self.browser.find_element(*inputs_sub_menu_selector)

    def buttons_sub_menu(self):
        return self.browser.find_element(*buttons_sub_menu_selector)

    def checkbox_sub_menu(self):
        return self.browser.find_element(*checkbox_sub_menu_selector)

    def select_sub_menu(self):
        return self.browser.find_element(*select_sub_menu_selector)

    def new_tab_sub_menu(self):
        return self.browser.find_element(*new_tab_sub_menu_selector)

    def next_area_sub_menu(self):
        return self.browser.find_element(*next_area_sub_menu_selector)

    def alerts_sub_menu(self):
        return self.browser.find_element(*alerts_sub_menu_selector)

    def drag_and_drop_sub_menu(self):
        return self.browser.find_element(*drag_and_drop_sub_menu_selector)

    def iframe_sub_menu(self):
        return self.browser.find_element(*iframe_sub_menu_selector)

    def pop_up_sub_menu(self):
        return self.browser.find_element(*pop_up_sub_menu_selector)

    def contact_link(self):
        return self.browser.find_element(*contact_link_selector)

    def whats_new_link(self):
        return self.browser.find_element(*whats_new_link_selector)

    def qa_practice_link(self):
        return self.browser.find_element(*qa_practice_link_selector)

    def text_input_click(self):
        return self.text_input().click()

    def simple_button_click(self):
        return self.simple_button().click()

    def single_checkbox_click(self):
        return self.single_checkbox().click()

    def text_area_click(self):
        return self.text_area().click()

    def select_input_click(self):
        return self.select_input().click()

    def single_ui_el_click(self):
        return self.single_ui_el().click()

    def inputs_sub_menu_click(self):
        return self.inputs_sub_menu().click()

    def buttons_sub_menu_click(self):
        return self.buttons_sub_menu().click()

    def checkbox_sub_menu_click(self):
        return self.checkbox_sub_menu().click()

    def select_sub_menu_click(self):
        return self.select_sub_menu().click()

    def new_tab_sub_menu_click(self):
        return self.new_tab_sub_menu().click()

    def next_area_sub_menu_click(self):
        return self.next_area_sub_menu().click()

    def alerts_sub_menu_click(self):
        return self.alerts_sub_menu().click()

    def drag_and_drop_sub_menu_click(self):
        return self.drag_and_drop_sub_menu().click()

    def iframe_sub_menu_click(self):
        return self.iframe_sub_menu().click()

    def pop_up_sub_menu_click(self):
        return self.pop_up_sub_menu().click()

    def contact_link_click(self):
        return self.contact_link().click()

    def whats_new_link_click(self):
        return self.whats_new_link().click()

    def homepage_click(self):
        return self.homepage().click()

    def qa_practice_link_click(self):
        return self.qa_practice_link().click()
