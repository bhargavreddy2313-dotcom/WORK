```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestSiteSwitchWithoutEstimate(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # Implicit wait for elements to be ready

    def test_site_switch_without_estimate(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Step 1: Login with valid credentials
        driver.get("https://example.com/login")  # Replace with the actual login URL
        username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "loginButton")

        username_input.send_keys("user7")
        password_input.send_keys("pass901")
        login_button.click()

        # Verify successful login by checking for a specific element on the homepage
        try:
            wait.until(EC.presence_of_element_located((By.ID, "homepageElement")))  # Replace with actual element ID
        except TimeoutException:
            self.fail("Login failed or homepage did not load correctly.")

        # Step 2: Attempt to switch sites without calculating estimate
        switch_site_button = wait.until(EC.element_to_be_clickable((By.ID, "switchSiteButton")))  # Replace with actual element ID
        switch_site_button.click()

        # Verify that the site switch is not allowed
        try:
            alert = wait.until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            self.assertIn("Estimate required", alert_text)  # Replace with actual alert text
        except TimeoutException:
            self.fail("Alert not displayed or site switch was incorrectly allowed.")

        # Step 3: Logout
        logout_button = wait.until(EC.element_to_be_clickable((By.ID, "logoutButton")))  # Replace with actual element ID
        logout_button.click()

        # Verify redirection to login page
        try:
            wait.until(EC.presence_of_element_located((By.ID, "loginButton")))  # Replace with actual login button ID
        except TimeoutException:
            self.fail("Logout failed or login page did not load correctly.")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```