from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def setup():
    option = Options()
    option.add_argument("--window-size=1280,720")
    option.add_argument("--headless")
    driver=webdriver.Chrome(options=option,executable_path="Driver/chromedriver.exe")
    return driver