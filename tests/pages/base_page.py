from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(10)
        self.browser.set_window_size(1920,1080)
        self.actions = ActionChains(self.browser)


    def actions_move_and_click(self, elem):
        self.actions.move_to_element(elem)
        self.actions.click(elem)
        self.actions.perform()

    def current_url(self):
        return self.browser.current_url

    @staticmethod
    def send_keys(elem, keys):
        elem.send_keys(keys)
        elem.send_keys('\ue007')

    def focus_new_tab(self):
        window = self.browser.window_handles
        self.browser.switch_to.window(window[-1])
