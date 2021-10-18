import pytest
import sys


@pytest.mark.skip
def test_login_scenario():
    print("Login done")

@pytest.mark.skipif(sys.version_info<(3,10), reason="Python version not supported")
def test_add_product():
    print("Add products")


@pytest.mark.xfail
def test_logout():
    assert False
    print("Logut")


def test_close_application():
    assert True
    print("Close the application")
