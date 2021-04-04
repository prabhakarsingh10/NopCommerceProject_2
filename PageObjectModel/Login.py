import json
from TestData import config

class LoginPOM:
    username_css="[value='admin@yourstore.com']"
    passward_css="[id='Password']"
    login_button_css="[type='submit']"
    file=open('TestData/Jsonfile.json')
    data=json.load(file)
    url=data['url']
    username=data['username']
    passward=data['passward']

    def login(self,driver):

        driver.find_element_by_css_selector(self.username_css).click()
        driver.find_element_by_css_selector(self.username_css).clear()
        driver.find_element_by_css_selector(self.username_css).send_keys(self.username)
        driver.find_element_by_css_selector(self.passward_css).click()
        driver.find_element_by_css_selector(self.passward_css).clear()
        driver.find_element_by_css_selector(self.passward_css).send_keys(self.passward)
        driver.find_element_by_css_selector(self.login_button_css).click()
        act_title = driver.title
        print(act_title)
        assert act_title == "Dashboard / nopCommerce administration"
        print("Login Successful")

