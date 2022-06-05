import unittest

from palindromo import Palindromo

class TestPalindromo(unittest.TestCase):
    __palindromo = None
    def setUp(self):
        self.__palindromo = Palindromo('Alex')
    def test_palindromo(self):
        self.assertTrue(self.__palindromo.esPalindromo())
    def test_palindromo2(self):
        self.__palindromo.setPalabra('anana')
        self.assertTrue(self.__palindromo.esPalindromo())
    def test_palindromo3(self):
        self.__palindromo.setPalabra('MENEM')
        self.assertTrue(self.__palindromo.esPalindromo())
if __name__ == '__main__':
    unittest.main()