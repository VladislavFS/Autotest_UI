from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import sys


@pytest.fixture(scope="module")
def browser():
    os = sys.platform
    if os == 'win32':
        return webdriver.Chrome()
    else:
        options = Options()
        options.add_argument('--headless')
        return webdriver.Chrome(options=options)
