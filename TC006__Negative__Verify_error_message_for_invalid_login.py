```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest

class TestInvalidLogin(unittest.TestCase):

    def setUp(self):
        # Initialize the ChromeDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # Implicit wait for 10 seconds

    def test_invalid_login(self):
        driver = self.driver
        # Step 1: Navigate to login page
        driver.get("http://example.com/login")  # Replace with the actual login page URL

        # Step 2: Enter invalid username and password
        username_field = driver.find_element(By.ID, "username")  # Replace with the actual username field ID
        password_field = driver.find_element(By.ID, "password")  # Replace with the actual password field ID

        username_field.send_keys("invalidUser")
        password_field.send_keys("wrongPass")

        # Step 3: Click Login
        login_button = driver.find_element(By.ID, "loginButton")  # Replace with the actual login button ID
        login_button.click()

        # Expected Result: Error message is displayed for invalid credentials
        try:
            # Wait for the error message to be visible
            error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "errorMessage"))  # Replace with the actual error message element ID
            )
            self.assertTrue(error_message.is_displayed(), "Error message is not displayed")
        except TimeoutException:
            self.fail("Error message did not appear within the expected time")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```