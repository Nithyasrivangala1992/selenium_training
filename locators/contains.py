import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(opts)
driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)
driver.find_elements("class name","ico-register").click()
time.sleep(2)
driver.find.element("class name",'ico-login').click()
time.sleep(2)
driver.find.element("class name",'ico-cart').click()