import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://staging.azalianow.shop/'
    browser.config.driver_name = 'chrome'
    browser.config.window_width = 1200
    browser.config.window_height = 1200
    yield

    browser.quit()
