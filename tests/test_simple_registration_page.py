from data.users import user
from pages.application import app


def test_simple_registration_form():
    app.left_panel.open_simple_registration_form()
    app.simple_registration.register(user)
    app.simple_registration.should_have_data(user)
