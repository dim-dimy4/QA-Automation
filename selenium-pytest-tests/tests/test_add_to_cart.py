import sys
import os

from selenium.webdriver.chrome.webdriver import WebDriver

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

def test_add_to_cart(browser: WebDriver):
    """Test adding an item to the cart."""
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Add item to cart
    login_page.add_item_to_cart()

    # Verify item is in the cart
    cart_badge = browser.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Item was not added to the cart!"
