import unittest

from parking_lot.src.app import create_parking_lot


class ParkingLotTest(unittest.TestCase):
    def test_file(self):
        pass

    def test_create_parking_lot(self):
        slots = 6
        create_parking_lot(slots)


if __name__ == "__main__":
    unittest.main()
