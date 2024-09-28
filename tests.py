import unittest
from station import *

class Tests(unittest.TestCase):
    def test_station_generation(self):
        library = Library()
        test_station = Station(library.Wares)
        self.assertIsNotNone(test_station.fuel_price)

    def test_ship_cargo(self):
        ship = Ship("Test",100,100,10)

        with self.subTest("Check empty cargo information"):
            self.assertEqual(ship.get_current_cargo_size(),0)
            self.assertEqual(ship.get_current_cargo_free_space(),100)

        ship.cargo.append(Ware("Test Ware",10,0,0,0,5,0))
        ship.cargo.append(Ware("Test Ware 2",5,0,0,0,3,0))

        with self.subTest("Check with 2 wares added"):
            self.assertEqual(ship.get_current_cargo_size(),65)
            self.assertEqual(ship.get_current_cargo_free_space(),35)
            self.assertEqual(ship.check_for_ware_in_cargo("Test Ware"),0)
            self.assertEqual(ship.check_for_ware_in_cargo("Test Ware 2"),1)

        ship.cargo.pop(1)

        with self.subTest("Check with one ware removed"):
            self.assertEqual(ship.get_current_cargo_free_space(),50)
            self.assertEqual(ship.check_for_ware_in_cargo("Test Ware 2"),None)



if __name__ == "__main__":
    unittest.main()