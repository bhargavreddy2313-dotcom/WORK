```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest
import time

class TestSiteSwitchFunctionality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode for faster execution
        chrome_options.add_argument("--disable-gpu")
        cls.driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.base_url = "https://example.com"  # Replace with the actual URL

    def setUp(self):
        self.driver.get(self.base_url)

    def test_site_switch_functionality(self):
        # Step 1: Login with valid credentials
        self.driver.find_element(By.ID, "username").send_keys("user4")
        self.driver.find_element(By.ID, "password").send_keys("pass012")
        self.driver.find_element(By.ID, "login-button").click()

        # Wait for the dashboard to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        # Step 2: Calculate an estimate
        self.driver.find_element(By.ID, "estimate-date").send_keys("2025-11-15")
        self.driver.find_element(By.ID, "calculate-button").click()

        # Step 3: View results
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "results"))
        )

        # Step 4: Click buttons to switch sites
        site_buttons = self.driver.find_elements(By.CLASS_NAME, "site-switch-button")
        for button in site_buttons:
            button.click()
            # Verify the site switch by checking the URL or a specific element
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("site-switched")  # Replace with actual condition
            )

        # Step 5: Logout
        self.driver.find_element(By.ID, "logout-button").click()

        # Verify user is redirected to login page
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-page"))
        )
        self.assertIn("login", self.driver.current_url)

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
```