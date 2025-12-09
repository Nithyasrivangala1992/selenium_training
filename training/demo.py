from attr import attributes
from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

"""
driver = webdriver.Chrome(opts)
driver.get("https://www.facebook.com/")
driver.find_element("id","email").send_keys("Hai Heloo")
time.sleep(2)
driver.find_element("id","pass").send_keys("How are you")
time.sleep(3)
driver.find_element("id","u_0_5_wb").click()
"""
# NoSuchElementException
"""
95% --> id value can be duplicate
        id value will not work
"""
# name:
# It is used to find the location of a particular webelement by using name attribute.
"""
Syntax:
        name = "value"
"""

# Sample Code:
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A1_html/sample.html")
driver.find_element("name","n1").send_keys("Email@gmail.com")
"""
"""
driver = webdriver.Chrome(opts)
driver.get("https://www.flipkart.com/")
time.sleep(3)
driver.find_element("name","q").send_keys("Iphone")
"""


# Tagname:
# It is used to find the location of an element by using tagname

# Html code consists of how many components:
"""
3 components
    1.tagname
    2.attributes
    3.text
<a href="https://www.facebook.com/" id="a1">Facebook</a>
"""
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A1_html/sample.html")
driver.find_element("tag name","input").send_keys("Password")
"""

"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A1_html/sample.html")
driver.find_element("tag name","a").click()
"""

"""driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A1_html/sample.html")
time.sleep(2)
driver.find_element("tag name","input").send_keys("Hello")
"""
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A1_html/sample.html")
time.sleep(2)
driver.find_element("tag name","a").click()
"""
# tag name with find_elements is a preferred comnination:

# 5.link text:
#     It is used to find the location of an element by using text.
#     It will work only for anchor Tag [It will work for span tag also but not all the time]
#     The text value is case sensitive

# Sample Html code:
# <a href="https://www.amazon.in">Amazon</a>
# <span>...</span>

# Sample code:
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A1_html/sample.html")
time.sleep(3)
driver.find_element("link text","Amazon").click()
"""

# was to click on minutes on flipkart.com
"""
driver = webdriver.Chrome(opts)
driver.get("https://www.flipkart.com/")
time.sleep(3)
driver.find_element("link text","Minutes").click()
"""
"""
driver = webdriver.Chrome(opts)
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element("tag name","input").send_keys("Password")
#ElementNotInteractableException
"""
"""
click on mac in https://www.apple.com/in/
Do signup in udemy
"""


