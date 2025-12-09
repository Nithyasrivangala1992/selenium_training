import time
from multiprocessing.resource_tracker import register

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://demowebshop.tricentis.com/register')
time.sleep(1)
class Register:

    def gender_btn(self):
        driver.find_element('id', 'gender-female').click()

    def firstname(self):
        driver.find_element('id', 'FirstName').send_keys('Nithya')

    def lastname(self):
        driver.find_element('id', 'LastName').send_keys('Vangala')

    def email(self):
        driver.find_element('id', 'Email').send_keys('Nithya@gmail.com')

    def pwd(self):
        driver.find_element('id', 'Password').send_keys('Nithya@123')

    def confirm_pwd(self):
        driver.find_element('id', 'ConfirmPassword').send_keys('Nithya@123')
reg = Register()
reg.gender_btn()
reg.firstname()
reg.lastname()
reg.email()
reg.pwd()
reg.confirm_pwd()
