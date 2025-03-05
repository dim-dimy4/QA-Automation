import pytest
from selenium import webdriver
import sys
import os

from selenium.webdriver.chrome.webdriver import WebDriver
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage  # Now Python will find pages

@pytest.fixture
def browser():
    """Fixture to initialize and quit the browser."""
    driver = webdriver.Chrome()  # Use Chrome
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_success(browser: WebDriver):
    """Test for successful login."""
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in browser.current_url, "Login failed!"

def test_login_fail(browser: WebDriver):
    """Test for unsuccessful login with incorrect password."""
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "wrong_password")

    error_message = login_page.get_error_message()
    assert "Epic sadface" in error_message, "Error message not displayed!"
