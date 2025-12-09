# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[2]/td[1]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[2]/td[2]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[2]/td[3]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[2]/td[4]').text)
#
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[3]/td[1]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[3]/td[2]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[3]/td[3]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[3]/td[4]').text)
#
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[4]/td[1]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[4]/td[2]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[4]/td[3]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[4]/td[4]').text)
#
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[5]/td[1]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[5]/td[2]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[5]/td[3]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[5]/td[4]').text)
#
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[6]/td[1]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[6]/td[2]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[6]/td[3]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[6]/td[4]').text)
#
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[7]/td[1]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[7]/td[2]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[7]/td[3]').text)
# print(driver.find_element('xpath','//table[@name="BookTable"]//tr[7]/td[4]').text)



import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)
for r in range(2, 8):
    for c in range(1, 5):
        data = driver.find_element('xpath', f'//table[@name="BookTable"]//tr[{r}]/td[{c}]')
        print(data.text, end='\t')
    print()
