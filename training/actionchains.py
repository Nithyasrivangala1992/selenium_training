# '''Mouse hovering operations''' : move to element

# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# opts.add_argument("--disable-notifications")
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# women = driver.find_element('xpath','(//a[text()="Women"])[1]')
# ac_obj.move_to_element(women).perform()
# time.sleep(2)
#
# Beauty = driver.find_element('xpath','//a[text()="Beauty"][1]')
# ac_obj.move_to_element(Beauty ).perform()
# time.sleep(2)
#
# Home = driver.find_element('xpath','//a[text()="Home"][1]')
# ac_obj.move_to_element(Home).perform()
# time.sleep(2)

# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
# driver.get('https://www.kushals.com/')
# time.sleep(2)
# accessories = driver.find_element('xpath', '(//a[contains(text(), "Accessories")])[2]')
# ac_obj.move_to_element(accessories).perform()
# time.sleep(2)
# wedding_store = driver.find_element('xpath', '(//a[contains(text(), "Wedding Store")])[2]')
# ac_obj.move_to_element(wedding_store).perform()

#'''hover to all the elments present  in the navigation bar'''
# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# navigation_elements = driver.find_element('xpath', '//a[@class="desktop-main"]')
# for ele in navigation_elements[:-1]:
#     ac_obj.move_to_element(ele).perform()
#     time.sleep(2)
#solution 2:
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# navigation_elements = driver.find_elements('xpath', '//a[@class="desktop-main"]')    ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]
# for ele in range(0, len(navigation_elements)-1):
#      ac_obj.move_to_element(navigation_elements[ele]).perform()
#      time.sleep(2)

'''Double click'''
from selenium.webdriver.common.utils import keys_to_typing
from trio import open_tcp_stream

from training.basics import driver

# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
# driver.get('https://testautomationpractice.blogspot.com/')
# copy_ele = driver.find_element('xpath','//button[text()="Copy Text"]')
# ac_obj.double_click(copy_ele).perform()
# time.sleep(2)
# email = driver.find_element('xpath','//label[text()="Email:"]')
# ac_obj.double_click(email).perform()
# time.sleep(2)

# '''Right click'''
# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
# driver.get('https://testautomationpractice.blogspot.com/')
# Dynamic = driver.find_element('xpath','//h2[text()="Dynamic Button"]')
# ac_obj.context_click(Dynamic).perform()
# time.sleep(2)

'''scrolling'''
# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# useful = driver.find_element('xpath','//p[text()=" USEFUL LINKS "]')
# ac_obj.scroll_to_element(useful).perform()
# time.sleep(2)

'''         Using execute_script        '''
# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# ref_ele = driver.find_element('xpath','//p[text()=" USEFUL LINKS "]')
# driver.execute_script("arguments[0].scrollIntoView();", ref_ele)

'''# ## Scrolling till the end of the application'''
# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome()
# ac_obj = ActionChains(driver)
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(3)
# # ## To go back to the start of the application
# ac_obj.send_keys(Keys.HOME).perform()

'''Using excute_script'''
# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# driver.get('https://www.myntra.com/')
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# time.sleep(3)
# driver.execute_script("window.scrollTo(0,-document.body.scrollHeight);")
# time.sleep(2)

# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)

'''     Scroll Down and scroll up by Pixels      
        SYNTAX  :   driver.execute_script("window.scrollBy(horizontal, vertical);")  
'''
# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,2000);")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,-2000);")
# time.sleep(2)

'''
Drag and drop
'''
# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# svg = driver.find_element('xpath','//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(svg).perform()
# time.sleep(2)
# drag_low = driver.find_element('xpath','//div[@id="draggable"]')
# drop_down = driver.find_element('xpath','//div[@id="droppable"]')
# ac_obj.drag_and_drop(drag_low,drop_down).perform()

'''SLIDER'''
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)
ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
ac_obj.scroll_to_element(ele).perform()
time.sleep(2)
slider = driver.find_element('xpath','//div[@id="slider-range"]/span[1]')
## Move the slider RIGHT by 200 pixels
ac_obj.click_and_hold(slider).move_by_offset(100, 0).release().perform()
time.sleep(2)
## Move the slider LEFT by 150 pixels
ac_obj.click_and_hold(slider).move_by_offset(-100,0).release().perform()
time.sleep(2)


