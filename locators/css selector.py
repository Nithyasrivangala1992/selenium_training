



# CSS SELECTOR:
# What is Css?
#     --> Css stands for Cascading style Sheet
#     --> It is used to decorate a webpage like color,font size,Background etc.....
# What is css selector?
#     It is used to find the location of a web element by using css expression
# css expression:

#syntax:
 #       tagname[attribute name='attribute value']
 #       Any attribute including id,name,class etcc....

# Where we have to write css expression?

#Step 1 : Inspect the element
#Step 2 : Press ctrl+f in your keyboard "find my string" search will get appear
#Step 3 : type the css expression

# Verify the css expression to check if the expression is valid or not:

#1.Element should get highlight
#2.code should get highlight in yellow color
#3.(1 of 1) Matching you have to get

#Sample code:

import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/login")
time.sleep(3)
driver.find_element("css selector","input[class='email']").send_keys("Amitabh mailto:bachhan@gmail.com")

