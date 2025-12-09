#import time
#from selenium import webdriver
#opts = webdriver.ChromeOptions()
#opts.add_experimental_option("detach", True)
#driver = webdriver.Chrome(opts)
#driver.get('https://demowebshop.tricentis.com/')
#time.sleep(2)
#footer_elements = driver.find_elements('xpath', '//div[@class="footer-menu-wrapper"]//a')
#print(footer_elements)          ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7, wb8, wb8,....wb22]
#for ele in footer_elements:
#    print(ele.text)

#import time
#from selenium import webdriver
#opts = webdriver.ChromeOptions()
#opts.add_experimental_option("detach", True)
#driver = webdriver.Chrome(opts)
#driver.get('https://demowebshop.tricentis.com/')
#time.sleep(2)
#categories = driver.find_elements('xpath', '//div[@class="block block-category-navigation"]//a')
#print(categories)       ## list of web-elements     ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]
#for ele in categories:
#  print(ele.text)

#import time
#from selenium import webdriver
#opts = webdriver.ChromeOptions()
#opts.add_experimental_option("detach", True)
#driver = webdriver.Chrome(opts)
#driver.get('https://www.myntra.com/')
#time.sleep(2)
#driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('adidas')
#time.sleep(2)
#driver.find_element('xpath', '//li[text()="Adidas Originals Shoes"]').click()
#time.sleep(2)
#adidas_shoes = driver.find_elements('xpath', '//h4[@class="product-product"]')      ## [wb1, wb2, wb3,..wb50]
#shoes_prices = driver.find_elements('xpath', '//div[@class="product-price"]')       ## [wb1, wb2, wb3,..wb50]
#for shoe, price in zip(adidas_shoes, shoes_prices):
#   print(shoe.text, "=", price.text)

import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://www.python.org/')
all_links = driver.find_elements('tag name','a')
for link in all_links:
    print(link.get_attribute('href'))


