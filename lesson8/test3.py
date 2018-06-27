def hello(name):
    return "Hello {}!".format(name)
    # 2 var:
  # return "Hello " + str(name) + "!"
  # return "Hello %s!" % name

def test_hello():
    assert hello("World") == "Hello World!"
    assert hello(1) == "Hello 1!"


test_hello()