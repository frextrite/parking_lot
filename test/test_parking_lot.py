import unittest

from parking_lot.src.app import create_parking_lot, lot


class ParkingLotTest(unittest.TestCase):
    def test_file(self):
        pass

    def test_create_parking_lot(self):
        expected_output = {1: False,
                           2: False,
                           3: False,
                           4: False,
                           5: False,
                           6: False}
        slots = 6
        create_parking_lot(slots)
        self.assertDictEqual(lot, expected_output)


if __name__ == "__main__":
    unittest.main()
