from PageObjectModel.Login import LoginPOM
from TestData import config
from selenium import webdriver

class Test_Login:
    def test_login(self):
        driver = config.setup()
        driver.get(LoginPOM.url)
        driver.maximize_window()
        ob=LoginPOM()
        ob.login(driver)
