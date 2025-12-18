
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest

class TestCostComparisonTable(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://ec2-13-203-252-128.ap-south-1.compute.amazonaws.com:32794/login"  # Replace with the actual URL

    def test_cost_comparison_table_display(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Step 1: Navigate to login page
        driver.get(f"{self.base_url}/login")

        # Step 2: Enter username and password
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
        password_field = driver.find_element(By.ID, "password")
        username_field.send_keys("user1")
        password_field.send_keys("pass123")

        # Step 3: Click Login
        login_button = driver.find_element(By.ID, "loginButton")
        login_button.click()

        # Step 4: Calculate an estimate
        estimate_button = wait.until(EC.element_to_be_clickable((By.ID, "calculateEstimate")))
        estimate_button.click()

        # Step 5: View results
        try:
            cost_comparison_table = wait.until(EC.visibility_of_element_located((By.ID, "costComparisonTable")))
            self.assertTrue(cost_comparison_table.is_displayed(), "Cost comparison table is not displayed")
        except TimeoutException:
            self.fail("Cost comparison table did not display within the timeout period")

        # Step 6: Logout
        logout_button = wait.until(EC.element_to_be_clickable((By.ID, "logoutButton")))
        logout_button.click()

        # Verify redirection to login page
        login_page_title = wait.until(EC.title_contains("Login"))
        self.assertTrue(login_page_title, "User was not redirected to login page after logout")

    def tearDown(self):
        # Teardown ChromeDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()