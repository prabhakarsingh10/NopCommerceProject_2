from selenium import webdriver
def setup():
    driver=webdriver.Chrome(executable_path="Driver/chromedriver.exe")
    return driver