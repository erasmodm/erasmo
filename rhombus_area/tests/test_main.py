# File: test_main.py
import unittest
from rhombus_area.main import main

class TestRombo(unittest.TestCase):
    def test_area_rombo(self):
        rombo = Rhombus(4, 6)
        self.assertEqual(rombo.area(), 12.0)

if __name__ == '__main__':
    unittest.main()
