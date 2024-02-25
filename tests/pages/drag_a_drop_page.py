from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

boxes_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[1]')
image_tab_selector = (By.XPATH, '//*[@id="content"]/ul/li[2]')
drag_me_selector = (By.XPATH, '//*[@id="rect-draggable"]')
drop_here_selector = (By.XPATH, '//*[@id="rect-droppable"]')
result_drop_selector = (By.XPATH, '//*[@id="text-droppable"]')
drag_image_selector = (By.XPATH, '//*[@id="rect-droppable1"]/img')
drop_image_selector = (By.XPATH, '//*[@id="rect-droppable2"]')
result_drop_image_selector = (By.XPATH, '//*[@id="rect-droppable2"]/p')


class DragAndDropPage(BasePage):

    def open_drag_drop_page(self):
        return self.browser.get('https://www.qa-practice.com/elements/dragndrop/boxes')

    def boxes_tab(self):
        return self.browser.find_element(*boxes_tab_selector)

    def image_tab(self):
        return self.browser.find_element(*image_tab_selector)

    def drag_me(self):
        return self.browser.find_element(*drag_me_selector)

    def drop_here(self):
        return self.browser.find_element(*drop_here_selector)

    def result_drop(self):
        return self.browser.find_element(*result_drop_selector)

    def drag_image(self):
        return self.browser.find_element(*drag_image_selector)

    def drop_image(self):
        return self.browser.find_element(*drop_image_selector)

    def result_drop_image(self):
        return self.browser.find_element(*result_drop_image_selector)

    def boxes_tab_click(self):
        return self.boxes_tab().click()

    def image_tab_click(self):
        return self.image_tab().click()

    def drag_and_drop(self, el_drag, el_drop):
        self.actions.drag_and_drop(el_drag, el_drop)
        self.actions.perform()
