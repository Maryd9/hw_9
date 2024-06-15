from pages.left_panel_page import LeftPanel
from pages.simple_registration_page import SimpleRegistrationPage


class Application:
    def __init__(self):
        self.simple_registration = SimpleRegistrationPage()
        self.left_panel = LeftPanel()


app = Application()