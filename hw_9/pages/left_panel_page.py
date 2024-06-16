from selene import browser, have
from selene.core import command


class LeftPanel:
    def __init__(self, app):
        self.tab_name = browser.all('.card-body')
        self.subtab_name = browser.all('li')
        self.app = app

    def open(self, tab_name, subtab_name):
        browser.all('.card-body').element_by(have.exact_text(tab_name)).perform(command.js.scroll_into_view).click()
        self.subtab_name.element_by(have.exact_text(subtab_name)).click()

    def open_simple_registration_form(self):
        self.app.open_browser()
        self.open('Elements', 'Text Box')
