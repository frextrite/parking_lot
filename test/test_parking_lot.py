import sys
import unittest

from io import StringIO

from parking_lot.src.app import create_parking_lot, lot


class ParkingLotTest(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_file(self):
        pass

    def test_create_parking_lot(self):
        slots = 6
        expected_output = {1: False,
                           2: False,
                           3: False,
                           4: False,
                           5: False,
                           6: False}
        expected_print = f"Created a parking lot with {slots} slots"
        create_parking_lot(slots)
        self.assertDictEqual(lot, expected_output)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_print)


if __name__ == "__main__":
    unittest.main()
