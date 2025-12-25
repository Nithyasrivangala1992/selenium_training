import time
class TestRegister():
       def test_reg_link(self,setup):
           setup.find_element('xpath','//a[text()="Register"]').click()

       def test_gender_btn(self,setup):
           setup.find_element('id','gender-female').click()

       def test_fname(self,setup):
           setup.find_element('id','FirstName').send_keys('Nithya')

       def test_lname(self,setup):
           setup.find_element('id','LastName').send_keys('Vangala')

       def test_reg_email(self,setup):
           setup.find_element('id','Email').send_keys('Nithay@gmail.com')

       def test_reg_pwd(self,setup):
           setup.find_element('id','Password').send_keys('Nithya@123')

       def test_confirm_pwd(self,setup):
           setup.find_element('id','ConfirmPassword').send_keys('Nithya@123')
           time.sleep(1)
