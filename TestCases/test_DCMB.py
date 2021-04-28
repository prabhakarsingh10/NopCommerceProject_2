from PageObjectModel.DashboardContentMinimizeButtton import DashboardMinimizeBitton
from selenium import webdriver
from TestData import config
from PageObjectModel.Login import LoginPOM
import time
class TestDCMB:
    def test_dcmb(self):
        driver=config.setup()
        driver.get(LoginPOM.url)
        driver.maximize_window()
        lg = LoginPOM()
        lg.login(driver)
        time.sleep(1)
        driver.find_element_by_xpath(DashboardMinimizeBitton.nopcommercenews_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(DashboardMinimizeBitton.commonstatistics_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(DashboardMinimizeBitton.orders_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(DashboardMinimizeBitton.newcustomers).click()
        time.sleep(1)
        driver.find_element_by_xpath(DashboardMinimizeBitton.ordertotals_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(DashboardMinimizeBitton.incompleteorders_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(DashboardMinimizeBitton.latestorders_xpaht).click()
        time.sleep(1)
        driver.find_element_by_xpath(DashboardMinimizeBitton.popularsearchkeywords_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(DashboardMinimizeBitton.bestsellerbyquality_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(DashboardMinimizeBitton.bestsellerbtamount_xpath).click()