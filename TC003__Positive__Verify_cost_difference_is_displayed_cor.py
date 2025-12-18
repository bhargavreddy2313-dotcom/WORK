```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest

class TestCostDifference(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless if needed
        cls.driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.base_url = "http://example.com"

    def setUp(self):
        self.driver.get(self.base_url)

    def test_verify_cost_difference(self):
        # Step 1: Login with valid credentials
        self.driver.find_element(By.ID, "username").send_keys("user3")
        self.driver.find_element(By.ID, "password").send_keys("pass789")
        self.driver.find_element(By.ID, "loginButton").click()

        # Wait for login to complete
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        # Step 2: Calculate an estimate
        self.driver.find_element(By.ID, "calculateEstimate").click()

        # Step 3: View results
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "results"))
        )

        # Step 4: Verify cost difference for each site
        cost_differences = self.driver.find_elements(By.CLASS_NAME, "cost-difference")
        for cost_difference in cost_differences:
            self.assertTrue(cost_difference.is_displayed(), "Cost difference is not displayed")

        # Step 5: Logout
        self.driver.find_element(By.ID, "logoutButton").click()

        # Verify redirection to login page
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginPage"))
        )
        self.assertIn("Login", self.driver.title)

    def tearDown(self):
        # Clear cookies after each test to ensure a clean state
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
```