# TestCase for ORANGE HRM Login test
# Launch Browser
# Verify Home page Title
# Verify Login
# Close browser
#When you create html test report then you should write on terminal "python <filename>"


import HtmlTestRunner
from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By

class OrangeHRMTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_HomepageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.assertEqual("OrangeHRM", self.driver.title, "Webpage title is not match")


    def test_Login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.assertEqual("OrangeHRM", self.driver.title, "Webpage title is not match")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Testcase is completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'C:\\Users\\LENOVO\Desktop\\SDET Selenium\\SDET SElenium Pytest\\SDET Unittest_HTML_POM\\Reports'))
    

