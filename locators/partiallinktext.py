#import time
#from selenium import webdriver
#opts = webdriver.ChromeOptions()
#opts.add_experimental_option("detach", True)
#driver = webdriver.Chrome(opts)
#driver.get("https://www.selenium.dev/downloads/")
#driver.maximize_window()
#time.sleep(2)
#driver.find_element("partial link text","languages").click()

# Python 3.14.0

import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(opts)
driver.get("file:///C:\Users\91949\Desktop/signup.html")
time.sleep(3)
driver.find_element("partial link text","Python").click()












