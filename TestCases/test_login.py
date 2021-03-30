from PageObjectModel.Login import LoginPOM
from TestData import config
from selenium import webdriver

class Test_Login:
    def test_login(self):
        ob=LoginPOM()
        ob.login()
