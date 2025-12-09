import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(opts)
driver.get('https://www.python.org/')
time.sleep(2)
driver.find_element('xpath','//a[text()="Downloads"]').click()
time.sleep(2)
driver.find_element('xpath','//a[text()="Python 3.10.19"]/../../../..//a[text()="Release Notes"]/../..')
time.sleep(2)

