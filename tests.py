import unittest
from station import *

class Tests(unittest.TestCase):
    def test_station_generation(self):
        library = Library()
        test_station = Station(library.Wares)
        self.assertIsNotNone(test_station.fuel_price)

if __name__ == "__main__":
    unittest.main()