from selenium.webdriver.common.by import By

class LoginPage:
    """Page Object class for the login page on SauceDemo."""

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        """Opens the login page."""
        self.browser.get("https://www.saucedemo.com/")

    def login(self, username, password):
        """Fills in username and password, then clicks the login button."""
        self.browser.find_element(By.ID, "user-name").send_keys(username)
        self.browser.find_element(By.ID, "password").send_keys(password)
        self.browser.find_element(By.ID, "login-button").click()

    def get_error_message(self):
        """Retrieves the error message if login fails."""
        return self.browser.find_element(By.CLASS_NAME, "error-message-container").text
    
    def add_item_to_cart(self):
        """Adds the first item to the cart."""
        self.browser.find_element(By.CLASS_NAME, "inventory_item").click()
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

