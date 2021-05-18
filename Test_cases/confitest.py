from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")




def pytest_configurations(config):
    config._metadata['project name'] = "Open_Cart"
    config._metadata['tester'] = "sreehari"
    config._metadata['module'] = "admin"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)