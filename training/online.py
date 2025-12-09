"""
from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/dd.html")
driver.maximize_window()
time.sleep(3)
"""
from os import times_result
from zipfile import sizeEndCentDir

from selenium.webdriver.common.devtools.v138.dom import get_attributes

# Way2:
"""
from selenium.webdriver import Chrome,ChromeOptions

opts = ChromeOptions()
opts.add_experimental_option("detach",True)
driver = Chrome(opts)
"""

from selenium import webdriver
# from selenium.webdriver.support.select import Select
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/dd.html")
driver.maximize_window()
time.sleep(3)
food_dropdown = driver.find_element("xpath","//select[@id='a1']")
ssd = Select(food_dropdown)
ssd.select_by_index(1)
"""
"""
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(opts)
driver.get("https://www.facebook.com/r.php?entry_point=login")
driver.maximize_window()
time.sleep(3)
day_dropdown = driver.find_element("xpath","//select[@id='day']")
ssd = Select(day_dropdown)
ssd.select_by_index(26)
"""

# from selenium.webdriver.support.select import Select
# obj = Select(arg)  #--> One Argument --> DropDown Address
"""
driver = webdriver.Chrome(opts)
driver.get("https://www.facebook.com/r.php?entry_point=login")
driver.maximize_window()
time.sleep(3)
month_dd = driver.find_element("id","month")
ssd = Select(month_dd)
# select_by_value(arg) --> arg --> Str
ssd.select_by_value("7")
"""

# To acheieve the standard dropdown we have use Select class
"""
SD
    SSD 

    MSD
NSD
"""
from selenium.webdriver.support.select import Select

"""
# Select(arg) --> Mandatory arg --> DD webelement
driver = webdriver.Chrome(opts)
month_dd = driver.find_element("id","month")
Select(month_dd)
"""
"""
driver = webdriver.Chrome(opts)
driver.get("https://www.facebook.com/r.php?entry_point=login")
driver.maximize_window()
time.sleep(3)
year_dd = driver.find_element("id","year")
ssd = Select(year_dd)
# select_by_visible_text(arg)  arg--> str
ssd.select_by_visible_text("1915")
"""

# MultiSelect DropDown:

# Selections Methods:
"""
select_by_index()
select_by_value()
select_by_visible_text()
"""
# Deselection Method:
"""
deselect_by_index()
deselect_by_value()
deselect_by_visible_text()
deselect_all()
"""

# from selenium.webdriver.support.select import Select
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/dd.html")
desserts_dd = driver.find_element("xpath","//select[@id='a2']")
msd = Select(desserts_dd)
# select By index:
time.sleep(3)
msd.select_by_index(4)
time.sleep(3)
# select by value
msd.select_by_value("m2")
time.sleep(3)
# select by text:
msd.select_by_visible_text("Truffle")

# deselect the options:
# deselect_by_index
# time.sleep(3)
# msd.deselect_by_index(4)
# deselect_by_value
# time.sleep(3)
# msd.deselect_by_value("m2")
# deselect_by_visible_text
# time.sleep(3)
# msd.deselect_by_visible_text("Truffle")
# time.sleep(3)
# msd.deselect_all()
"""
"""
driver = webdriver.Chrome(options=opts)
driver.get("https://demoapps.qspiders.com/ui/dropdown/multiSelect?sublist=1&scenario=2")
time.sleep(3)
dd = driver.find_element("xpath","//select[@id='select-multiple-native']")
msd = Select(dd)
time.sleep(3)
msd.select_by_index(2)
time.sleep(3)
msd.select_by_value("SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s")
time.sleep(3)
driver.find_element("xpath","//button[text()='Add']").click()
"""
# is_multiple:
#     It is used to check of the dropdown is multi select or not if it is then it will give the output as True else None
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/dd.html")
msd = driver.find_element("id","a2")
dd = Select(msd)
print(dd.is_multiple)
#True
"""
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/dd.html")
ssd = driver.find_element("id","a1")
dd = Select(ssd)
print(dd.is_multiple)
#None
"""
# options:
"""
    It is used to return all the option from the drop down
    It will return the list of option address
"""
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/dd.html")
ssd = driver.find_element("id","a1")
dd = Select(ssd)
print(dd.options)

[<selenium.webdriver.remote.webelement.WebElement (session="41f722f0bf0336359dbf87fa46b72fb1", element="f.369EEFE63BEF1477EBF4555178E8E49C.d.706C119569EF1C36CB87217952EB4DED.e.4")>, <selenium.webdriver.remote.webelement.WebElement (session="41f722f0bf0336359dbf87fa46b72fb1", element="f.369EEFE63BEF1477EBF4555178E8E49C.d.706C119569EF1C36CB87217952EB4DED.e.6")>, <selenium.webdriver.remote.webelement.WebElement (session="41f722f0bf0336359dbf87fa46b72fb1", element="f.369EEFE63BEF1477EBF4555178E8E49C.d.706C119569EF1C36CB87217952EB4DED.e.8")>, <selenium.webdriver.remote.webelement.WebElement (session="41f722f0bf0336359dbf87fa46b72fb1", element="f.369EEFE63BEF1477EBF4555178E8E49C.d.706C119569EF1C36CB87217952EB4DED.e.10")>, <selenium.webdriver.remote.webelement.WebElement (session="41f722f0bf0336359dbf87fa46b72fb1", element="f.369EEFE63BEF1477EBF4555178E8E49C.d.706C119569EF1C36CB87217952EB4DED.e.12")>]

"""
# to get the exact option as an output:
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/dd.html")
ssd = driver.find_element("id","a1")
dd = Select(ssd)
data = dd.options
# text: --> It is used to extract the text from the webelement
for i in data:
    print(i.text)

"""
"""
driver = webdriver.Chrome(opts)
driver.get("https://www.facebook.com/r.php?entry_point=login")
month = driver.find_element("id","month")
dd = Select(month)
data = dd.options
for i in data:
    print(i.text)
driver.close()
"""
# Was to extract the options only if it is startswith vowels:
"""
driver = webdriver.Chrome(opts)
driver.get("https://www.facebook.com/r.php?entry_point=login")
month = driver.find_element("id","month")
dd = Select(month)
data = dd.options
l = []
for i in data:
    if i.text[0] in 'aeiouAEIOU':
        l.append(i.text)
print(l)
driver.close()
"""
# was to extract the odd dates from the facebook.com
"""
driver = webdriver.Chrome(opts)
driver.get("https://www.facebook.com/r.php?entry_point=login")
time.sleep(3)
day = driver.find_element("id","day")
ssd = Select(day)
data = ssd.options
# print(data)
out = []
for i in data:
    # print(i.text,type(i.text))
    if int(i.text)%2 == 1:
        out.append(i.text)
print(out)
driver.close()
# ['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27', '29', '31']
"""
# all_selected_options:
from selenium.webdriver.support.select import Select

'''
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/dd.html")
time.sleep(3)
desserts_dd = driver.find_element("id","a2")
msd = Select(desserts_dd)
msd.select_by_index(0)
time.sleep(1)
msd.select_by_index(2)
time.sleep(1)
msd.select_by_index(4)
time.sleep(3)
data = msd.all_selected_options
# print(data)  #--> Address of webelements in the form of list
for i in data:
    print(i.text)
'''

# first_selected_option:
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/dd.html")
time.sleep(3)
desserts_dd = driver.find_element("id","a2")
msd = Select(desserts_dd)
msd.select_by_index(4)
msd.select_by_index(2)
msd.select_by_index(0)
msd.select_by_value("m1")
msd.select_by_visible_text("Ghevar")
data = msd.first_selected_option
# print(data)
print(data.text)  #Truffle
driver.close()
"""

"""
{'A':['Agra','Ajmer'....],'B':['Banglore',"ballari"......],"C":[.....],'D'}
"""




