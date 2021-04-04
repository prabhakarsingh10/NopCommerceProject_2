from TestData import config
from PageObjectModel.NavbarMenu import NavbarMenu
from PageObjectModel.Login import LoginPOM
class TestNavbarMenu:

    def test_navbar_menu(self):
        driver = config.setup()
        driver.get(LoginPOM.url)
        driver.maximize_window()
        lg=LoginPOM()
        lg.login(driver)
        driver.find_element_by_xpath(NavbarMenu.catalog_xpath).click()


