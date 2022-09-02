class Login():
    def __init__(self,driver):
       self.driver=driver
       self.username_name='uid''
       self.password_name='password'
       self.submit='btnLogin'
    def enter_username(self,username):
       self.driver.find_element_by_name(self.username_name).clear()
       self.driver.find_element_by_name(self.username_name).send_keys(username)
    def enter_password(self,password):
       self.driver.find_element_by_name(password_name).clear()
       self.driver.find_element_by_name(password_name).send_keys(password)
    def login_click(self):
       self.driver.find_element_by_name(submit).click()