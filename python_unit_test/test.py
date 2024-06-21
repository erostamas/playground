import unittest

class TestMyFlaskApp(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.__x = 3
        print("this is setUpClass")

    def setUp(self):
        print("this is setUp")

    def test_one(self):
        print(f"this is test_one {self.__x}")

    def test_two(self):
        print("this is test_two")

if __name__ == '__main__':
    unittest.main()

