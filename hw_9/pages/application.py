from selene.support.shared import browser
from hw_9.pages.left_panel_page import LeftPanel
from hw_9.pages.simple_registration_page import SimpleRegistrationPage


class Application:
    def __init__(self):
        self.simple_registration = SimpleRegistrationPage()
        self.left_panel = LeftPanel(self)

    def open_browser(self):
        browser.open('/')
        return self


app = Application()
