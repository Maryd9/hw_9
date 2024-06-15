from selene import browser, have


class LeftPanel:
    def __init__(self):
        self.tab_name = browser.all('.card-body>h5')
        self.subtab_name = browser.all('li')

    def open(self, tab_name, subtab_name):
        element = self.tab_name.element_by(have.exact_text(tab_name))
        browser.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", element())
        self.subtab_name.element_by(have.exact_text(subtab_name)).click()

    def open_simple_registration_form(self):
        self.open('Elements', 'Text Box')
