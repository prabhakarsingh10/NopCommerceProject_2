from PageObjectModel.Login import LoginPOM
from selenium import webdriver
def setup():
    driver=webdriver.Chrome(executable_path="Driver/chromedriver.exe")
    driver.get(LoginPOM.url)
    driver.maximize_window()
    return driver
