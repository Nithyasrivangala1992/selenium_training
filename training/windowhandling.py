# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(15)
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# time.sleep(12)
# driver.find_element('xpath','//a[text()="Google+"]').click()
# time.sleep(2)
# def handling_windows():
#     return driver.window_handles
# for handle in handling_windows():
#     driver.switch_to.window(handle)
#     if 'googleblog' in driver.current_url:
#         driver.find_element('xpath','//input[@class="header__search"]').send_keys('IPHONE 16 PRO')
#         time.sleep(2)
#         driver.switch_to.window(handling_windows()[0])
#         time.sleep(2)
# driver.find_element('xpath','//a[text()="YouTube"]').click()
# time.sleep(2)
# for handle in handling_windows():
#     driver.switch_to.window(handle)
#     if 'user' in driver.current_url:
#         driver.find_element('xpath','(//div[@class="yt-spec-touch-feedback-shape__fill"])[6]').click()

import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(opts)
driver.implicitly_wait(15)
driver.get('https://www.flipkart.com/')
time.sleep(2)
driver.find_element('xpath','//input[@title="Search for Products, Brands and More"]').send_keys('phones under 30000')
time.sleep(2)
driver.find_element('xpath','//button[@type="submit"]').click()
time.sleep(2)
driver.find_element('xpath','//div[@class="KzDlHZ"]').click()
def handle_window():
     return driver.window_handles
 for handle in handle_window():
     driver.switch_to.window(handle)
     if 'samsung-galaxy-f36-5g-red-128-gb' in driver.current_url:
         driver.find_element('xpath','//button[text()="Add to cart"]').click()
         time.sleep(2)

driver.find_element('xpath','//a[text()="Help Center"]').click()
time.sleep(2)
for handle in handle_window():
    driver.switch_to.window(handle)
     if 'helpcentre' in driver.current_url:
         driver.find_element('xpath','//a[text()="Know more"]').click()

#
# driver.find_element('xpath', '//a[text()="Twitter"]').click()
# time.sleep(2)
# for handle in handling_windows():
#     driver.switch_to.window(handle)
#     if 'x.com' in driver.current_url:
#         driver.find_element('xpath', '//span[text()="Follow"]').click()


