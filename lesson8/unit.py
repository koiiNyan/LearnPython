import unittest
from welcome import hello

class TestHello(unittest.TestCase):
    def test_hello_bob(self):
        self.assertEqual(hello("Bob"), "Hello Bob!")

    def test_hello_number(self):
        self.assertEqual(hello(1), "Hello Bob!")

    def test_hello_anon(self):
        self.assertEqual(hello(None), "Hello!")