```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import unittest
import time

class TestLogoutFunctionality(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode for faster execution
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
        self.driver.get("http://example.com/login")  # Replace with the actual login URL
        self.wait = WebDriverWait(self.driver, 10)

    def test_logout_functionality(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Login with valid credentials
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "loginButton")

        username_field.send_keys("user5")
        password_field.send_keys("pass345")
        login_button.click()

        # Step 2: Calculate an estimate
        estimate_button = wait.until(EC.element_to_be_clickable((By.ID, "calculateEstimate")))
        estimate_button.click()

        # Step 3: View results
        results_section = wait.until(EC.visibility_of_element_located((By.ID, "results")))
        self.assertTrue(results_section.is_displayed(), "Results section is not displayed")

        # Step 4: Logout
        logout_button = wait.until(EC.element_to_be_clickable((By.ID, "logoutButton")))
        logout_button.click()

        # Expected Result: User is logged out and redirected to login page
        login_page_title = wait.until(EC.title_contains("Login"))
        self.assertTrue(login_page_title, "User is not redirected to the login page after logout")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```