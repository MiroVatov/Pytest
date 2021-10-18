
import pytest

@pytest.mark.smoke  # cutom marker
def test_login_scenario():
    print("Login done")


@pytest.mark.regression
def test_add_product():
    print("Add products")


@pytest.mark.smoke
def test_logout():
    print("Logut")