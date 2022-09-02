from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import unittest
from Automation Test scrpits.pages.Login_page import Login
from Automation Test scrpits.pages.Logout_page import Logout
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",'..'))
class guru_acount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
         cls.driver=webdriver.Chrome()
         cls.driver.implicitly_wait(10)
         cls.driver.maximize_window()

    def test_login_page(self):
        self.driver.get('http://demo.guru99.com/V4/')
        login=Login(self.driver)
        login.enter_username('mngr190727')
        login.enter_password('UbavunA')
        login.login_click()
    def test_home_page(self):
        print(self.driver.title)
    def test_logout_page(self):
        logout=Logout(self,driver)
        logout.click_logout()
    @classmethod
    def tearDownClass(cls):
       #.time.sleep(5)
       cls.driver.close()
       cls.driver.quit()
if __name__ == "__main__":
    unittest.main()