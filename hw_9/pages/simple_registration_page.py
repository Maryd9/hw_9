from selene import browser, have, command
from hw_9.data.users import User


class SimpleRegistrationPage:
    def __init__(self):
        self.full_name_element = browser.element('#userName')
        self.email_element = browser.element('#userEmail')
        self.current_address_element = browser.element('#currentAddress')
        self.permanent_address_element = browser.element('#permanentAddress')
        self.submit_button_element = browser.element('#submit')

    def fill_full_name(self, value):
        self.full_name_element.type(value)

    def fill_email(self, value):
        self.email_element.type(value)

    def fill_current_address(self, value):
        self.current_address_element.type(value)

    def fill_permanent_address(self, value):
        self.permanent_address_element.type(value)

    def submit(self):
        self.submit_button_element.perform(command.js.scroll_into_view).click()

    def register(self, user: User):
        self.fill_full_name(user.full_name)
        self.fill_email(user.email)
        self.fill_current_address(user.current_address)
        self.fill_permanent_address(user.permanent_address)
        self.submit()
        return self

    def should_have_data(self, user: User):
        browser.all('#output').all('p').should(
            have.exact_texts(
                f"Name:{user.full_name}",
                f"Email:{user.email}",
                f"Current Address :{user.current_address}",
                f"Permananet Address :{user.permanent_address}"))
        return self
