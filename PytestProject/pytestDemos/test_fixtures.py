"""
    pytest fixtures: provides setup services, state or other operation environments, and thers is no need each time to set up this preconditions

    Precondition
        Setup, Connection, API

    Run Test

    Run Test

    Assertions ....

    Postconsition
        clean, close


"""

import pytest


@pytest.fixture
def setup():
    print("Start browser")
    yield
    print("Close browser")

def test_one(setup):
    print("Test 1 executed")

def test_two(setup):
    print("Test 2 executed")

def test_three(setup):
    print("Test 3 executed")

