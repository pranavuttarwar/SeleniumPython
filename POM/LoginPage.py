from selenium.webdriver.common.by import By


class LoginPage:

    #declar locators globally
    Username = "//input[@id='user-name']"
    Password = "//input[@id='password']"
    Login = "//input[@id='login-button']"

    #Create constructor for web driver call
    def __init__(self, driver):  #Need to create the constructor for browser call
        self.driver = driver   #Convert the local varibale into class variable using self.<varibale name>


    #Perform Actions
    def login(self,uname):
        self.driver.find_element(By.XPATH, self.Username).send_keys(uname)

    def password(self,pas):
        self.driver.find_element(By.XPATH, self.Password).send_keys(pas)

    def login(self):
        self.driver.find_element(By.XPATH, self.Login).click()