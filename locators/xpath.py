# xpath :
#xpath is used to find the location of a webelement in a html tree structure or in DOM(Document object Model)
#xpath classified into two types:
# 1.Absolute xpath
# 2.Relative xpath
# 1.Absolute xpath
#     -->It will traverse from parent to its own child
#     -->It is Denoted as (/)
# Drawbacks of Absolute xpath
#     -->Absolute xpath is very lengthy comparing to relative xpath
#     --> Always it will traverse from parent to its own child
# 2.Relative xpath
#     -->It will traverse from parent to any of the child
#     -->It is Denoted as (//)
# Sample for Absolute xpath

#import time
#from selenium import webdriver
#opts = webdriver.ChromeOptions()
#opts.add_experimental_option("detach",True)
#driver = webdriver.Chrome(opts)
#driver.get("C:\Users\91949\Desktop/xpath.html")
#time.sleep(3)
#driver.find_element("xpath","html/body/div[1]/input[1]").send_keys("Username1")


#import time
#from selenium import webdriver
#opts = webdriver.ChromeOptions()
#opts.add_experimental_option("detach",True)
#driver = webdriver.Chrome(opts)
#driver.get("https://demowebshop.tricentis.com/")
#time.sleep(3)
#driver.find_element("xpath","html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").click()

#import time
#from selenium import webdriver
#opts = webdriver.ChromeOptions()
#opts.add_experimental_option("detach", True)
#driver = webdriver.Chrome(opts)
#driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M15-Aug11\files_\css_selector_dup.html')
#time.sleep(2)
#driver.find_element('xpath', 'html/body/input[1]').send_keys('Amit')
#time.sleep(1)
#driver.find_element('xpath', 'html/body/input[2]').send_keys('amit@12345')

import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://www.saucedemo.com/')
time.sleep(2)
driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('standard_user')
time.sleep(1)
driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('secret_sauce')
time.sleep(1)
driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/input').click()