def hello(name):
    return "Hello " + name + "!"


def test_hello():
    assert hello("World") == "Hello World!"


test_hello()

#name = input("Enter your name: ")
#print(hello(name))