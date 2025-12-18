
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest

class TestCheapestSiteBadge(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.base_url = "http://ec2-13-203-252-128.ap-south-1.compute.amazonaws.com:32794/login"  # Replace with the actual URL

    def test_cheapest_site_badge(self):
        driver = self.driver
        driver.get(self.base_url)

        # Step 1: Login with valid credentials
        driver.find_element(By.ID, "username").send_keys("alexsingh")
        driver.find_element(By.ID, "password").send_keys("demo123")
        driver.find_element(By.XPATH,("//button[normalize-space()='Sign In']")).click()

        # Step 2: Calculate an estimate
        # Assuming there's a date picker and a calculate button
        date_field = driver.find_element(By.ID, "claim_service_date")
        date_field.clear()
        date_field.send_keys("2025-11-29")
        date_field.send_keys(Keys.RETURN)
        driver.find_element(By.ID, "calculateButton").click()

        # Step 3: View results
        # Wait for results to load
        results_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsTable"))
        )

        # Step 4: Check for badge on cheapest site
        # Assuming the badge has a specific class or attribute
        cheapest_site_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cheapest-badge"))
        )
        self.assertTrue(cheapest_site_badge.is_displayed(), "Cheapest site badge is not displayed")

        # Step 5: Logout
        driver.find_element(By.ID, "logoutButton").click()

        # Verify user is redirected to login page
        login_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginPage"))
        )
        self.assertTrue(login_page.is_displayed(), "User is not redirected to login page after logout")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
