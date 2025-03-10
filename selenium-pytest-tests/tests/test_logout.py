import sys
import os

from selenium.webdriver.chrome.webdriver import WebDriver

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

def test_logout(browser: WebDriver):
    """Test successful logout."""
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Wait until the menu button becomes clickable
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    ).click()

    # Wait until the logout button becomes clickable
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()
    print("Current URL after logout:", browser.current_url)

    # Wait for the login form to appear (indicating successful logout)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )

    # Verify that the login form is actually visible
    assert browser.find_element(By.ID, "user-name").is_displayed(), "Logout failed!"


