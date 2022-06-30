from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 

class SeleniumDo:
    __TIMEOUT = 30
 
    def __init__(self, driver):
        super(SeleniumDo, self).__init__()
        self._driver_wait = WebDriverWait(driver, SeleniumDo.__TIMEOUT)
        self._driver = driver
 
    def open(self, url):
        self._driver.get(url)
 
    def maximize(self):
        self._driver.maximize_window()        
        
    def close(self):
        self._driver.quit()
         
    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_xpath_invisible(self, xpath):
        return self._driver_wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
 
    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))
 
    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id))) 
         
    def find_by_class(self, classname):
        return self._driver_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, classname))) 
    
    def click_js_xpath(self, xpath):
        button = self._driver.find_element_by_xpath(xpath)
        self._driver.execute_script("arguments[0].click();", button)