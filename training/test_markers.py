'''


'''

import pytest

# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"
# ## collected 4 items / 2 deselected / 2 selected
# ## test_markers.py::test_signup    signup executing       PASSED
# ## test_markers.py::test_reg       reg executing           PASSED

###################################################################################

# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.regression
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"               --> test_login and test_logout will execute
# ## pytest test_markers.py -vs -m="smoke"                --> test_signup will execute
# ## pytest test_markers.py -vs -m="regression"           --> test_reg will execute
# ## pytest test_markers.py -vs -m="sanity and smoke"     --> 0 executed
# ## pytest test_markers.py -vs -m="sanity and regression"--> 0 executed
# ## pytest test_markers.py -vs -m="smoke and regression" --> 0 executed
# ## pytest test_markers.py -vs -m="sanity or regression" --> test_login, test_reg and test_logout will execute
# ## pytest test_markers.py -vs -m="smoke or regression"  --> test_signup and test_reg will execute
# ## pytest test_markers.py -vs -m="sanity and smoke"     --> test_login, test_signup and test_logout will execute


###################################################################################

@pytest.mark.smoke
@pytest.mark.sanity
def test_login():
    print("login executing")

@pytest.mark.smoke
def test_signup():
    print("signup executing")

@pytest.mark.sanity
@pytest.mark.regression
def test_reg():
    print("reg executing")

@pytest.mark.smoke
@pytest.mark.regression
def test_logout():
    print("logout executing")

## In terminal
## pytest test_markers.py -vs -m="sanity"                   --> test_login and test_teg will execute
## pytest test_markers.py -vs -m="smoke"                    --> test_login, test_signup and test_logout
## pytest test_markers.py -vs -m="regression"               --> test_reg and test_logout
## pytest test_markers.py -vs -m="smoke and sanity"         --> test_login will exceute
## pytest test_markers.py -vs -m="smoke and regression"     --> test_logout will execute
## pytest test_markers.py -vs -m="sanity and regression"    --> test_reg will execute
## pytest test_markers.py -vs -m="smoke or sanity"          --> all 4 will execute
## pytest test_markers.py -vs -m="smoke or regression"      --> all 4 will execute
## pytest test_markers.py -vs -m="sanity or regression"     --> test_login, test_signup and test_logout will execute

###################################################################################

@pytest.mark.sanity
class TestSample:

    def test_login(self):
        print("login executing")

    def test_reg(self):
        print("reg executing")

    def test_signup(self):
        print("signup executing")

    def test_logout(self):
        print("logout executing")

## All the attributes of the TestSample class belongs to sanity

###################################################################################

class TestSample:

    @pytest.mark.sanity
    def test_login(self):
        print("login executing")

    def test_reg(self):
        print("reg executing")

    @pytest.mark.smoke
    def test_signup(self):
        print("signup executing")

    @pytest.mark.sanity
    def test_logout(self):
        print("logout executing")
































