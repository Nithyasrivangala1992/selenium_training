
import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get("https://www.purplle.com")
time.sleep(2)
driver.find_element("link text","OFFERS").click()
driver.find_element("tag name", "input").send_keys("Prashant")
time.sleep(1)
driver.find_element("tag name", "input").send_keys("Naveen")























