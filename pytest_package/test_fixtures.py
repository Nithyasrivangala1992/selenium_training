# '''Decorator'''
# def outer(fun):
#     def wrapper(*args,**kargs):
#         print("Hello Miss World")
#         func(*args,**kargs)
#     return wrapper
#
# @outer
# def add(a, b):
#     print(a+b)
# add(20,30)

##############################################################################

# def outer(func):
#      def wrapper(*args,**kargs):
#          print("Hello Miss World")
#          func(*args,**kargs)
#          func(*args,**kargs)
#      return wrapper
#
# @outer
# def test_login():
#      print("Hello Universe")
#
# @outer
# def test_logout():
#      print("Hello World")
# ##############################################################################
# '''
# Fixtures    :   They are the functions which are used to perform setup and teardown operations
#                 setup       :   The set of operations which executes before the execution of the test_function
#                 teardown    :   The set of operations which executes afetr the execution of the test_function
#
#                 SYNTAX  :       @pytest.fixture()
#                                 def func():
#                                     pass        ## setup
#                                     yield
#                                     pass        ## teardown
#
#                                 def test_func(func):
#                                     pass
#'''
# ##############################################################################

# import pytest
# @pytest.fixture()
# def greet():
#     print("Welcome to selenium")
#
# def test_login(greet):
#     print("Login successful")
#
# def test_logout(greet):
#     print("Logout successful")
# ##############################################################################

# import pytest
# @pytest.fixture()
# def greet():
#      print("Hello world")
#
# def test_login(greet):
#      print("Login successful")
#
# def test_signup():
#      print("signup successful")
#
# def test_logout(greet):
#      print("Logout successful")

'''
Fixture is not applied for test_signup.
'''
from tarfile import TruncatedHeaderError

################################################################
# import pytest
# @pytest.fixture()
# def greet():
#      print("Good morning")               ## setup
#      yield
#      print("Good evening")               ## teardown
#
# def test_login(greet):
#      print("login successful")
#
# def test_signup(greet):
#      print("signup successful")
#
# def test_logout(greet):
#      print("logout successful")
'''
NOTE    :   The operations before yield will execute before the execution of the test_function
            The operations after yield will execute after the execution of the test_function
'''
################################################################
# import pytest
# @pytest.fixture(autouse=True)
# def greet():
#      print("Good morning")               ## setup
#      yield
#      print("Good evening")               ## teardown
#
# def test_login():
#      print("login successful")
#
# def test_signup():
#      print("signup successful")
#
# def test_logout():
#     print("logout successful")
# ################################################################
# import pytest
# @pytest.fixture()
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#      def test_login(self, greet):
#          print("login successful")
#
#      def test_signup(self, greet):
#          print("signup successful")
#
#      def test_logout(self, greet):
#          print("logout successful")
################################################################
# import pytest
# @pytest.fixture(autouse=True)
# def greet():
#      print("Good morning")               ## setup
#      yield
#      print("Good evening")               ## teardown
#
# class TestSample:
#
#      def test_login(self):
#          print("login successful")
#
#      def test_signup(self):
#          print("signup successful")
#
#      def test_logout(self):
#          print("logout successful")
################################################################
# import pytest
# @pytest.fixture(autouse=True, scope='class')
# def greet():
#      print("Good morning")               ## setup
#      yield
#      print("Good evening")               ## teardown
#
# class TestSample:
#
#      def test_login(self):
#          print("login successful")
#
#      def test_signup(self):
#          print("signup successful")
#
#      def test_logout(self):
#          print("logout successful")

'''
scope is the parameter of the fixture.
When we give scope='class', the fixture will be applied on a class level.
*   It will perform the setup operation.
*   It will execute all the attributes of the TestClass
*   It will perform the teardown operation
'''
################################################################

# import pytest
# @pytest.fixture(autouse=True, scope='class')
# def greet():
#      print("Good morning")               ## setup
#      yield
#      print("Good evening")               ## teardown
#
# class TestSample:
#
#      def test_login(self):
#          print("login successful")
#
#      def test_signup(self):
#          print("signup successful")
#
# class TestSpam:
#
#      def test_reg(self):
#          print("reg successful")
#
#      def test_logout(self):
#          print("logout successful")
################################################################

# import pytest
# @pytest.fixture(autouse=True, scope='class')
# def greet():
#      print("Good morning")               ## setup
#      yield
#      print("Good evening")               ## teardown
#
#
# def test_gmail():
#      print("gmail successful")
#
# class TestSample:
#
#      def test_login(self):
#          print("login successful")
#
#      def test_signup(self):
#          print("signup successful")
#
# class TestSpam:
#
#      def test_reg(self):
#          print("reg successful")
#
#      def test_logout(self):
#          print("logout successful")
################################################################
# import pytest
# @pytest.fixture(autouse=True, scope='module')
# def greet():
#       print("Good morning")               ## setup
#       yield
#       print("Good evening")               ## teardown
#
# def test_gmail():
#       print("gmail successful")
#
# class TestSample:
#
#       def test_login(self):
#           print("login successful")
#
#       def test_signup(self):
#           print("signup successful")
#
# class TestSpam:
#
#       def test_reg(self):
#           print("reg successful")
#
#       def test_logout(self):
#          print("logout successful")
################################################################################################
# import pytest
# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture(scope='class')
# def setup():
#     driver = webdriver.Chrome(opts)
#     driver.get('https://demowebshop.tricentis.com/')
#     time.sleep(2)
#     yield driver
#     driver.close()
#
# class TestRegister():
#
#       def test_reg_link(self,setup):
#           setup.find_element('xpath','//a[text()="Register"]').click()
#
#       def test_gender_btn(self,setup):
#           setup.find_element('id','gender-female').click()
#
#       def test_fname(self,setup):
#           setup.find_element('id','FirstName').send_keys('Nithya')
#
#       def test_lname(self,setup):
#           setup.find_element('id','LastName').send_keys('Vangala')
#
#       def test_reg_email(self,setup):
#           setup.find_element('id','Email').send_keys('Nithay@gmail.com')
#
#       def test_reg_pwd(self,setup):
#           setup.find_element('id','Password').send_keys('Nithya@123')
#
#       def test_confirm_pwd(self,setup):
#           setup.find_element('id','ConfirmPassword').send_keys('Nithya@123')
#           time.sleep(1)
#
# class TestLogin:
#       def test_login_link(self,setup):
#           setup.find_element('xpath','//a[text()="Log in"]').click()
#
#       def test_login_email(self,setup):
#           setup.find_element('id','Email').send_keys('Nithya@gmail.com')
#
#       def test_login_pwd(self,setup):
#           setup.find_element('id','Password').send_keys('Nithya@123')

################################################################################################

import time
import pytest
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

@pytest.fixture(autouse=True,  scope='class')
def setup():
    driver = webdriver.Chrome(opts)
    driver.get('https://www.demoblaze.com/')
    time.sleep(2)
    yield driver
    driver.close()

class Testlogin:
      def test_login(self,setup):
          setup.find_element('xpath','//a[text()="Log in"]').click()
      def test_uname(self,setup):
          setup.find_element('id',"loginusername").send_keys('Nithya@gmail.com')
      def test_pwd(self,setup):
          setup.find_element('id','loginpassword').send_keys('Nithya@123')

class Testsignup:
      def test_signup(self,setup):
          setup.find_element('xpath','//a[text()="Sign up"]').click()
          time.sleep(2)
      def test_signup_uname(self,setup):
          setup.find_element('xpath','//input[@id="sign-username"]').send_keys('Nithya@gmail.com')
      def test_signup_pwd(self,setup):
          setup.find_element('id','sign-password').send_keys('Nithya@123')