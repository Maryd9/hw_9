import pytest
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.open('/')

    yield

    browser.quit()
