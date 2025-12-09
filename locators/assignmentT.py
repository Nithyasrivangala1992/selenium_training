#import time
#from selenium import webdriver
#opts = webdriver.ChromeOptions()
#opts.add_experimental_option("detach",True)
#driver = webdriver.Chrome(opts)
#driver.get('https://www.myntra.com/')
#time.sleep(2)
#driver.find_element("xpath",'(//a[@class="desktop-main"])[2]').click()
#time.sleep(2)
#result = driver.find_elements("xpath",'//div[@class="desktop-popularSearch"]//a')
#print(result)
#for web in result:
#  print(web.text)

# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# driver.find_element("xpath",'//input[@class="desktop-searchBar"]').send_keys('adidas')
# time.sleep(2)
# driver.find_element('xpath', '//li[text()="Adidas Originals Shoes"]').click()
# time.sleep(2)
# driver.find_element("xpath",'//div[@class="colour-more"]').click()
# output = driver.find_elements("xpath",'//span[@class="colour-label colour-colorDisplay"]')
# print(output)
# for web in output:
#     print(web.text)

import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(opts)
driver.get('https://www.zomato.com/nizamabad')
time.sleep(2)
driver.find_element("xpath",'//p[text()="Pizza - Delivery"]').send_keys('Pizza.-.Delivery')
time.sleep(2)

driver.find_element("xpath",'//p[text()="Pizza.-.Delivery"]').click()
driver.find_element("xpath",'//h4[@class="sc-1hp8d8a-0.sc-Ehqfj.bxOQva"]').click()
time.sleep(2)


# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# driver.get('https://in.bookmyshow.com/explore/home/nizamabad')
# #driver.find_element("xpath",'//span[text()="Detect my location"]').click()
# time.sleep(2)
# movie_elements = driver.find_elements('xpath','//div[@class="sc-7o7nez-0 lkwOqB"]')
# for movie in movie_elements:
#     print(movie.text)