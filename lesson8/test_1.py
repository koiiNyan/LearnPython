def hello():
    return "Hi!"

def test_hello():
    assert hello() == "Hi!"


def hello2():
    return "Noon!"

def test_hello2():
    assert hello2() == "Hello!"

test_hello()
test_hello2()

