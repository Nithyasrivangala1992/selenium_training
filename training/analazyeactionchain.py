'''
ANALYZE THE BELOW CODE
'''

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element('xpath', '//input[@name="firstname"]').send_keys('Harry')
time.sleep(1)

ac_obj.send_keys(Keys.TAB).perform()        ## The control will shift to the lastname
time.sleep(1)
ac_obj.send_keys('Potter').perform()
time.sleep(2)

ac_obj.send_keys(Keys.BACKSPACE).perform()
time.sleep(2)
ac_obj.send_keys(Keys.BACKSPACE).perform()

# ##-------------------------------------------------------------------

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

fname = driver.find_element('xpath', '//input[@name="firstname"]')
lname = driver.find_element('xpath', '//input[@name="lastname"]')

fname.send_keys('Harry')
time.sleep(2)

fname.send_keys(Keys.CONTROL + 'a')         ## select the data
fname.send_keys(Keys.CONTROL + 'c')         ## copy the data

ac_obj.send_keys(Keys.TAB).perform()        ## switching the control to last name
lname.send_keys(Keys.CONTROL + 'v')         ## paste the data

# ##-------------------------------------------------------------------

## ctrl + a
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)
ac_obj.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()

# ############################################################################################################

## ctrl + backspace
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)
driver.find_element('xpath', '//input[@id="name"]').send_keys('Harry Potter')
time.sleep(2)
ac_obj.key_down(Keys.CONTROL).send_keys(Keys.BACKSPACE).key_up(Keys.CONTROL).perform()

# ##-------------------------------------------------------------------

## shift
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)
driver.find_element('xpath', '//input[@id="name"]').send_keys('harry')
time.sleep(2)
ac_obj.key_down(Keys.SHIFT).send_keys('a').perform()

# ##-------------------------------------------------------------------

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

driver.find_element('xpath', '//input[@id="name"]').send_keys('Harry Potter')
time.sleep(2)
ac_obj.send_keys(Keys.TAB).perform()
time.sleep(2)
ac_obj.send_keys('harry@gmail.com').perform()


'''
Go to https://crossbrowsertesting.github.io/drag-and-drop.html, perform drag and drop
'''