class Logout():
    def __init__(self,driver):
       self.driver=driver
       self.logout_name='Log out'
    def click_logout(self):
       self.driver.find_element_by_link_text('Log out').click()
