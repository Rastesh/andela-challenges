import unittest
from ship import Ship

class Testship(unittest.TestCase):
    def test_hello(self):
        draft = 40
        crew = 5
        expected = True

        ship = Ship(draft, crew)
        result= ship.is_worth_it()

        assert result == expected

if __name__ == '__main__':
    unittest.main()