from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from util.selenium_func import SeleniumDo
import undetected_chromedriver as uc

 
def get_browser(browser):
    if browser == "chrome":
        s = Service("./chromedriver")
        #driver = webdriver.Chrome(service=s) #normal chrome driver (blocks bot log in to google)
        driver = uc.Chrome(version_main=100) #undetected chrome dirver (allows bot log in to google)
        return SeleniumDo(driver)