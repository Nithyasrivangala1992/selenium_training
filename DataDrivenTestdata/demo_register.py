import time
from selenium import webdriver
from DataDrivenTestdata.read_excel import reading_testdata
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(opts)
driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)
path = r'C:\Users\91949\Desktop\python seleniumM16\demo_testdata.xlsx'
data = reading_testdata(path,'Sheet1' )
driver.find_element('xpath','//a[text()="Register"]').click()
time.sleep(2)
driver.find_element('id','gender-female').click()
driver.find_element('id','FirstName').send_keys(data['firstname'])
driver.find_element('id','LastName').send_keys(data['latsname'])
driver.find_element('id','Email').send_keys(data['email'])
driver.find_element('id','Password').send_keys(data['pwd'])
driver.find_element('id','ConfirmPassword').send_keys(data['conpwd'])
