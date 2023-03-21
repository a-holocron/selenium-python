import pytest
from selenium import webdriver


@pytest.fixture(scope='class', autouse=True)
def set_up(request):
    print('Setup from pytest')
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
