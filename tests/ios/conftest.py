from appium.options.ios import XCUITestOptions
import pytest
import os
from cfg import config
from appium import webdriver
import allure
import allure_commons
from selene import browser, support


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = XCUITestOptions().load_capabilities({
        # Укажите платформу и версию ОС для тестирования
        'platformName': 'iOS',
        'platformVersion': '17',
        'deviceName': 'iPhone 15',

        # Укажите путь к приложению для тестирования
        'app': 'bs://sample.app',

        # Укажите другие возможности BrowserStack
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            'userName': config.bstack_userName,
            'accessKey': config.bstack_accessKey,
        }
    })

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub',
            options=options
        )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield
    browser.quit()
