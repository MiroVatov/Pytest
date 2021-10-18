def test_1():
    x = 10
    y = 100
    assert x==y

def test_2():
    name="Selenium"
    title="Selenium is for web automation"
    assert name in title

def test_3():
    name="jenkins"  # failed test
    title="Jenkins is CI server"
    assert name in title , "Title does not match"  # second argument is displayed if the assertion returns False