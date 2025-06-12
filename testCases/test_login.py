import pytest
from selenium import webdriver
from pageObjects.Loginpage import LoginPage
from selenium.webdriver.common.by import By
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    #call the customLogger loggen function which is static method
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("**************Test_001_Login*************")
        self.logger.info("**************Verify Home Page Title*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        #Just change the act title and run the program and see the error msg scrn shrt is uploaded in the screenshot directory
        if act_title == "nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************Home Page title Test is passed*************")
        else:
            self.driver.save_screenshot(os.path.join(".\\Screenshots\\"+"test_homePageTitle.png"))
            self.driver.close()
            self.logger.error("**************Home Page title Test is Failed*************")
            assert False

    def test_login(self, setup):
        self.logger.info("**************Verifying Login Test*************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        #Creating Object
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        expected_title = "Dashboard / nopCommerce administration123"
        print("Current Page Title:", act_title)

        # Just change the act title and run the program and see the error msg screenshot is uploaded in the screenshot directory
        if act_title == expected_title:
            assert True
            self.logger.info("**************Login Test is passed*************")
            self.driver.close()

        else:
            self.driver.save_screenshot(os.path.join(".\\Screenshots\\" + "test_login.png"))
            self.driver.close()
            self.logger.error("**************Login Test is Failed*************")
            assert False



