from selenium import webdriver
import pytest


@pytest.fixture(scope="module")
def browser():
    return webdriver.Chrome()\


