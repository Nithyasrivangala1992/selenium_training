'''
Dependency  :   We can create the dependencies between the testcases.
                One testcase can be dependent on other testcases.

                To install dependency   -->     pip install pytest-dependency

                SYNTAX  :   @pytest.mark.dependency()               ## Independent testcase
                            def test_func1():
                                pass

                            @pytest.mark.dependency(depends=['test_func1'])         ## Dependent testcase
                            def test_func2():
                                pass

                            test_func2 is dependent on test_func1

                            If the independent testcase executes without any error, then dependent also executes without any error
                            If independent testcase itself is not working fine, then the dependent testcase will be skipped


'''
# import time
# import pytest
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
# @pytest.mark.dependency()                   ## independent testcase
# def test_login():
#      driver.find_element("id", "user-name").send_keys('standard_user')
#      time.sleep(1)
#      driver.find_element('id', 'password').send_keys('secret_sauceeeee')
#      time.sleep(1)
#      driver.find_element('id', 'login-button').click()
#      time.sleep(3)
#
#      assert 'inventory' in driver.current_url
#
#
# @pytest.mark.dependency(depends=['test_login'])     ## dependent testcase
# def test_logout():
#      driver.find_element('id', 'react-burger-menu-btn').click()
#      time.sleep(2)
#      driver.find_element('id', 'logout_sidebar_link').click()

###################################################################################################
# import time
# import pytest
# @pytest.mark.dependency()
# def test_login():
#      print("login successful")
#
# @pytest.mark.dependency(depends=['test_login'])
# def test_logout():
#      print("logout successful")
#
# # ## collected 2 items
# # ## test_depends.py::test_login     login successful         PASSED
# # ## test_depends.py::test_logout    logout successful        PASSED

###################################################################################################
# import time
# import pytest
# @pytest.mark.dependency()
# def test_login():
#      raise Exception
#
# @pytest.mark.dependency(depends=['test_login'])
# def test_logout():
#      print("logout successful")
#
# ## test_depends.py::test_login     FAILED
# ## test_depends.py::test_logout    SKIPPED (test_logout depends on test_login)

###################################################################################################
# import time
# import pytest
# @pytest.mark.dependency()
# def test_login():
#      print("login successful")
#
# @pytest.mark.dependency()
# def test_reg():
#      print("reg successful")
#
# @pytest.mark.dependency(depends=['test_login', 'test_reg'])
# def test_logout():
#      print("logout successful")
#
# # ## collected 3 items
# # ## test_depends.py::test_login     login  successful     PASSED
# # ## test_depends.py::test_reg       reg    successful     PASSED
# # ## test_depends.py::test_logout    logout successful     PASSED

###################################################################################################
# import time
# import pytest
# @pytest.mark.dependency()
# def test_login():
#      print("login successful")
#
# @pytest.mark.dependency()
# def test_reg():
#      print("reg successful")
#
# @pytest.mark.dependency(depends=['test_login', 'test_reg'])
# def test_logout():
#      print("logout successful")
#
# # ## collected 3 items
# # ## test_depends.py::test_login     login successful     PASSED
# # ## test_depends.py::test_reg                            FAILED
# # ## test_depends.py::test_logout                         SKIPPED (test_logout depends on test_reg)


###################################################################################################
# import time
# import pytest
# @pytest.mark.dependency()
# def test_reg():
#      print("reg successful")
#
# @pytest.mark.dependency(depends=['test_reg'])
# def test_login():
#      print("login successful")
#
# @pytest.mark.dependency(depends=['test_login'])
# def test_logout():
#      print("logout successful")
#
# # ## collected 3 items
# # ## test_depends.py::test_reg       reg    successful       PASSED
# # ## test_depends.py::test_login     login  successful       PASSED
# # ## test_depends.py::test_logout    logout successful       PASSED

###################################################################################################
# import time
# import pytest
# @pytest.mark.dependency()
# def test_reg():
#      print("reg successful")
#
# @pytest.mark.dependency(depends=['test_reg'])
# def test_login():
#      print("login successful")
#
# @pytest.mark.dependency(depends=['test_login'])
# def test_logout():
#      print("logout successful")
#
# # ## collected 3 items
# # ## test_depends.py::test_reg       FAILED
# # ## test_depends.py::test_login     SKIPPED (test_login depends on test_reg)
# # ## test_depends.py::test_logout    SKIPPED (test_logout depends on test_login)

##########################################################################################################
# import time
# import pytest
# class TestSample:
#
#      @pytest.mark.dependency()                                           ## independent testcase
#      def test_login(self):
#          print("login successful")
#
#      @pytest.mark.dependency(depends=['test_login'])                     ## dependent testcase
#      def test_logout(self):
#          print("logout successful")
#
# # ## collected 2 items
# # ## test_depends.py::TestSample::test_login         login executing     PASSED
# # ## test_depends.py::TestSample::test_logout                            SKIPPED (test_logout depends on test_login)

'''
pytest will look for test_login in the global area(outside class).
There is no test_login in the global area, thats why test_logout is skipped
'''

##########################################################################################################
# import time
# import pytest
# class TestSample:
#
#      @pytest.mark.dependency()                                           ## independent testcase
#      def test_login(self):
#          print("login successful")
#
#      @pytest.mark.dependency(depends=['TestSample::test_login'])                     ## dependent testcase
#      def test_logout(self):
#          print("logout successful")
#
# # ## collected 2 items
# # ## test_depends.py::TestSample::test_login     login successful         PASSED
# # ## test_depends.py::TestSample::test_logout    logout successful        PASSED
