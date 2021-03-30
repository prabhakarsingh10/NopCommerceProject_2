from PageObjectModel.Login import LoginPOM
from TestData import config


class Test_Login:
    def test_login(self):
        driver = config.setup()
        driver.find_element_by_css_selector(LoginPOM.username_css).click()
        driver.find_element_by_css_selector(LoginPOM.username_css).send_keys(LoginPOM.username)
        driver.find_element_by_css_selector(LoginPOM.passward_css).click()
        driver.find_element_by_css_selector(LoginPOM.passward_css).send_keys(LoginPOM.passward)
        driver.find_element_by_css_selector(LoginPOM.login_button_css).click()
