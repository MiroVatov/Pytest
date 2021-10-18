import pytest
import sys


@pytest.mark.parametrize("username,password", [("Selenium", "WebDriver"),
                                               ("Python", "Pytest"),
                                               ("Miro", "totalmikro")] )
def test_login(username,password):
    print(username)
    print(password)
