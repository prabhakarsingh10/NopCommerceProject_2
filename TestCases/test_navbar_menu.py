from TestData import config
import time
from PageObjectModel.NavbarMenu import NavbarMenu
from PageObjectModel.Login import LoginPOM
class TestNavbarMenu:

    def test_navbar_menu(self):
        driver = config.setup()
        driver.get(LoginPOM.url)
        driver.maximize_window()
        lg=LoginPOM()
        lg.login(driver)
        #1
        driver.find_element_by_xpath(NavbarMenu.catalog_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.catalog_xpath).click()
        #2
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.sales_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.sales_xpath).click()
        #3
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.customer_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.customer_xpath).click()
        #4
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.promotions_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.promotions_xpath).click()
        #5
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.content_management_xpth).click()
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.content_management_xpth).click()
        #6
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.configuration_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.configuration_xpath).click()
        #7
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.system_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.system_xpath).click()
        #8
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.reports_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.reports_xpath).click()
        #9
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.help_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(NavbarMenu.help_xpath).click()



