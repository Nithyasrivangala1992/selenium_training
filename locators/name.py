import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome()
driver.get('https://www.facebook.com/reg/')
time.sleep(2)
driver.find_element('name','firstname').send_keys('Nithya')
time.sleep(2)
