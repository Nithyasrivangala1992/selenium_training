'''
Markers     :   To group the testcases, we use markers

There are 2 types of markers
    *   custom markers
    *   Inbuilt markers :   There are 4 types
                            *   skip
                            *   skipif
                            *   parametrize
                            *   xfail

'''
from pickle import FALSE

# import pytest
# def test_login():
#     print("login successful")
#
# @pytest.mark.fall
# def test_reg():
#     print("reg successful")
#
# @pytest.mark.fall
# def test_signup():
#     print("signup successful")
#
# def test_logout():
#     print("logout successful")
#
# # In terminal
# # pytest  test_markers.py - vs - m = "fall" ---> reg and signup successful
##########################################################################################################

# import pytest
# @pytest.mark.fall
# def test_login():
#     print("login successful")
#
# @pytest.mark.cool
# def test_reg():
#     print("reg successful")
#
# @pytest.mark.fall
# def test_signup():
#     print("signup successful")
#
# @pytest.mark.chill
# def test_logout():
#     print("logout successful")
#
# # # In terminal
# # pytest test_markers.py -vs -m="fall"               --->  login and signup successful                   PASSED
# # pytest test_markers.py -vs -m="cool"               --->  reg successful                                PASSED
# # pytest test_markers.py -vs -m="chill"              --->  logout successful                             PASSED
# # pytest test_markers.py -vs -m="cool and fall"      --->  0
# # pytest test_markers.py -vs -m="chill and fall"     --->  0
# # pytest test_markers.py -vs -m="chill and cool"     --->  0
# # pytest test_markers.py -vs -m="not fall"           --->  reg and logout successful                      PASSED
# # pytest test_markers.py -vs -m="not cool"           --->  login,signup and logout successful             PASSED
# # pytest test_markers.py -vs -m="not chill"          --->  login,reg and signup successful                PASSED

##########################################################################################################

# import pytest
# @pytest.mark.fall
# @pytest.mark.cool
# def test_login():
#      print("login successful")
#
# @pytest.mark.chill
# @pytest.mark.cool
# def test_reg():
#      print("reg successful")
#
# @pytest.mark.fall
# def test_signup():
#      print("signup successful")
#
# @pytest.mark.cool
# @pytest.mark.chill
# def test_logout():
#      print("logout successful")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="fall"               --->  login and signup successful                   PASSED
# ## pytest test_markers.py -vs -m="cool"               --->  login,reg,logout successful                   PASSED
# ## pytest test_markers.py -vs -m="chill"              --->  reg,logout successful                         PASSED
# ## pytest test_markers.py -vs -m="cool and fall"      --->  login successful                              PASSED
# ## pytest test_markers.py -vs -m="fall or cool"       --->  0
# ## pytest test_markers.py -vs -m="fall or chill"      --->  0
# ## pytest test_markers.py -vs -m="cool or chill"      --->  0
# ## pytest test_markers.py -vs -m="chill and fall"     --->  4                                             PASSED
# ## pytest test_markers.py -vs -m="chill and cool"     --->  reg,logout                                    PASSED
# ## pytest test_markers.py -vs -m="not fall"           --->  reg and logout successful                     PASSED
# ## pytest test_markers.py -vs -m="not cool"           --->  signup successful                             PASSED
# ## pytest test_markers.py -vs -m="not chill"          --->  login and signup successful                   PASSED

##########################################################################################################

# import pytest
# @pytest.mark.fall
# class TestSample:
#
#      def test_login(self):
#          print("login successful")
#
#      def test_reg(self):
#          print("reg successful")
#
#      def test_signup(self):
#          print("signup successful")
#
#      def test_logout(self):
#          print("logout successful")

# ## collected 4 items
# login successful  PASSED
# reg successful    PASSED
# signup successful PASSED
# logout successful PASSED
##########################################################################################################
# import pytest
# @pytest.mark.fall
# class TestSample:
#
#      @pytest.mark.cool
#      def test_login(self):
#          print("login successful")
#
#      def test_reg(self):
#          print("reg successful")
#
#      @pytest.mark.chill
#      def test_signup(self):
#          print("signup successful")
#
#      def test_logout(self):
#          print("logout successful")
# # ## In terminal
# # ## pytest test_markers.py -vs -m="fall"                  ---> All 4 successful
# # ## pytest test_markers.py -vs -m="cool"                  ---> login successful
# # ## pytest test_markers.py -vs -m="chill"                 ---> signup successful
# # ## pytest test_markers.py -vs -m="fall and cool"         ---> 0
# # ## pytest test_markers.py -vs -m="fall and chill"        ---> signup successful
# # ## pytest test_markers.py -vs -m="cool and chill"        ---> 0
# # ## pytest test_markers.py -vs -m="fall or cool"          ---> All 4 successful
# # ## pytest test_markers.py -vs -m="fall or chill"         ---> All 4 successful
# # ## pytest test_markers.py -vs -m="cool or chill"         ---> login and reg successful
#

##########################################################################################################
# import pytest
# @pytest.mark.fall
# class TestSample:
#
#      def test_login(self):
#          print("login successful")
#
#      def test_reg(self):
#          print("reg successful")
#
#
# @pytest.mark.chill
# class TestExample:
#
#      def test_signup(self):
#          print("signup successful")
#      def test_logout(self):
#          print("logout successful")


#########################################################################################################
'''
skip    :   To skip the execution of the testcases, we use skip marker
            It is an unconditional skip. To skip the testcases we dont have to pass any reason or condition.
            Reason is optional parameter.
            It will skip the testcases which are decorated with @pytest.mark.skip

            SYNTAX  :   @pytest.mark.skip
                        def test_case():
                            pass 
'''

# import time
# import pytest
# @pytest.mark.skip
# def test_login():
#      print("login successful")
#
# def test_reg():
#      print("reg successful")
#
# def test_signup():
#      print("signup successful")
#
# @pytest.mark.skip
# def test_logout():
#     print("logout successful")
#
# ## collected 4 items
# ## test_markers.py::test_login                             SKIPPED (unconditional skip)
# ## test_markers.py::test_reg           reg executing       PASSED
# ## test_markers.py::test_signup        signup executing    PASSED
# ## test_markers.py::test_logout                            SKIPPED (unconditional skip)


###############################################################################################
# import time
# import pytest
# def test_login():
#      print("login successful")
#
# @pytest.mark.skip(reason="reg already done")
# def test_reg():
#      print("reg successful")
#
# @pytest.mark.skip(reason="signup already done")
# def test_signup():
#      print("signup successful")
#
# def test_logout():
#      print("logout successful")
#
# ## collected 4 items
# ## test_markers.py::test_login                 login executing     PASSED
# ## test_markers.py::test_reg                                       SKIPPED (reg already done)
# ## test_markers.py::test_signup                                    SKIPPED (signup already done)
# ## test_markers.py::test_logout                logout executing    PASSED

###############################################################################################
# import time
# import pytest
# @pytest.mark.skip
# class TestSample:
#
#     def test_login(self):
#         print("login successful")
#
#     def test_reg(self):
#         print("reg successful")
#
#     def test_signup(self):
#         print("signup successful")
#
#     def test_logout(self):
#         print("logout successful")
#
# ## collected 4 items
# ## test_markers.py::TestSample::test_login     SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_reg       SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_signup    SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_logout    SKIPPED (unconditional skip)

###############################################################################################
'''
skipif  :   skipif is also used to skip the execution of the testcases, but the skip is based on a condition.
            It takes two parameters, condition and reason.
            condition is the first parameter, reason is the second parameter.
            Both are mandatory parameters

            SYNTAX  :   @pytest.mark.skipif(condition, reason)
                        def test_case():
                            pass

                        If the condition is True, it will skip the execution of the testcase
                        If the condition is False, it will execute the testcase 

# '''
# import time
# import pytest
# @pytest.mark.skipif(True,reason='login already done')
# def test_login():
#     print("login successful")
# ##In Terminal
# ##test_login SKIPPED (login already done)
####################################################################################################

# import time
# import pytest
# @pytest.mark.skipif(False,reason='reg already done')
# def test_reg():
#     print("reg successful")
###################################################################################################

# import time
# import pytest
# @pytest.mark.skipif(False)
# def test_reg():
#     print("reg successful")
#
# ## test_markers.py::test_login         ERROR
# ## In the above testcase, reason is not specified, thats why its giving error.
# ## reason is the mandatory parameter
###################################################################################################

# import time
# import pytest
# @pytest.mark.skiprif(reason='reg already completed')
# def test_reg():
#      print("reg successful")
# # ##In Terminal
# # ##test_markers.py::  test_reg reg successful        PASSED
###################################################################################################

# import time
# import pytest
# @pytest.mark.skipif(reason="login already completed")
# def test_login():
#      print("login successful")
#
# ## collected 1 item
# ## test_markers.py::test_login     SKIPPED (login already completed)
# ## When the condition is not gives, by default it will be considered as True.
# ## That's why the testcase is skipped when no conditions are given
###################################################################################################

'''
skip    :
'''
import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
driver.get('https://www.saucedemo.com/')
time.sleep(2)
def test_login():
     driver.find_element("id", "user-name").send_keys('standard_user')
     time.sleep(1)
     driver.find_element('id', 'password').send_keys('secret_sauce')
     time.sleep(1)
     driver.find_element('id', 'login-button').click()
     time.sleep(3)

def test_logout():
    if 'inventory' not in driver.current_url:
        pytest.skip("login is unsuccessfull")

        driver.find_element('id', 'react-burger-menu-btn').click()
        time.sleep(2)
        driver.find_element('id', 'logout_sidebar_link').click()

