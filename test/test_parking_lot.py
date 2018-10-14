import sys
import unittest

from io import StringIO
from unittest.mock import patch

from parking_lot.src.app import create_parking_lot, park
from parking_lot.src.app import LOT, R_NO_COLOR, SLOT_NO_REG, SLOT_NO_COLOR


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
        self.assertDictEqual(LOT, expected_output)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_print)

    @patch.dict(LOT, {1: False}, clear=True)
    def test_park(self):
        registration_number = "KA-01-HH-1234"
        color = "White"
        park(registration_number, color)
        self.assertDictEqual(R_NO_COLOR, {color: registration_number})
        self.assertDictEqual(SLOT_NO_REG, {registration_number: 1})
        self.assertDictEqual(SLOT_NO_COLOR, {color: [1]})


if __name__ == "__main__":
    unittest.main()
