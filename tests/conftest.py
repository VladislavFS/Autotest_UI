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
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        return webdriver.Chrome(options=options)
