import sys
import unittest

from io import StringIO
from unittest.mock import patch

from parking_lot.src.app import (create_parking_lot, 
                                 park,
                                 leave,
                                 status,
                                 registration_numbers_for_cars_with_colour,
                                 slot_numbers_for_cars_with_colour,
                                 slot_number_for_registration_number)
from parking_lot.src.app import DATA, LOT, R_NO_COLOR, SLOT_NO_REG, SLOT_NO_COLOR


class ParkingLotTest(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_file(self):
        pass

    @patch.dict(LOT, {}, clear=True)
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

    @patch.dict(LOT, {1: True, 2: False, 3: True, 4: False, 5: False}, clear=True)
    @patch.dict(DATA, {}, clear=True)
    def test_park(self):
        registration_number = "KA-01-HH-1234"
        color = "White"
        park(registration_number, color)
        self.assertDictEqual(DATA, {2: {'registration_number': registration_number, 'color': color}})
        self.assertDictEqual(R_NO_COLOR, {color: [registration_number]})
        self.assertDictEqual(SLOT_NO_REG, {registration_number: 2})
        self.assertDictEqual(SLOT_NO_COLOR, {color: [2]})
        self.assertEqual(sys.stdout.getvalue().strip(), f"Allocated slot number: 2")

    @patch.dict(LOT, {1: True, 2: True, 3: True, 4: True, 5: True}, clear=True)
    @patch.dict(DATA, {}, clear=True)
    def test_park_full(self):
        registration_number = "KA-01-HH-1234"
        color = "White"
        park(registration_number, color)
        self.assertEqual(sys.stdout.getvalue().strip(), f"Sorry, parking lot is full")

    @patch.dict(LOT, {1: False, 2: True}, clear=True)
    @patch.dict(DATA, {2: {'registration_number': "KA-01-HH-1234", 'color': "White"}}, clear=True)
    @patch.dict(R_NO_COLOR, {"White": ["KA-01-HH-1234"]}, clear=True)
    @patch.dict(SLOT_NO_REG, {"KA-01-HH-1234": 2}, clear=True)
    @patch.dict(SLOT_NO_COLOR, {"White": [2]}, clear=True)
    def test_leave(self):
        slot = 2
        registration_number = "KA-01-HH-1234"
        color = "White"

        leave(slot)
        self.assertDictEqual(R_NO_COLOR, {color: []})
        self.assertDictEqual(SLOT_NO_REG, {})
        self.assertDictEqual(SLOT_NO_COLOR, {color: []})
        self.assertEqual(sys.stdout.getvalue().strip(), f"Slot number {slot} is free")

    @patch.dict(LOT, {1: False, 2: True, 3: False, 4: True}, clear=True)
    @patch.dict(DATA, {2: {'registration_number': "KA-01-HH-1234", 'color': "White"}, 4: {'registration_number': "KA-01-HH-9999", 'color': "White"}}, clear=True)
    @patch.dict(R_NO_COLOR, {"White": ["KA-01-HH-1234", "KA-01-HH-9999"]}, clear=True)
    @patch.dict(SLOT_NO_REG, {"KA-01-HH-1234": 2, "KA-01-HH-9999": 4}, clear=True)
    @patch.dict(SLOT_NO_COLOR, {"White": [2, 4]}, clear=True)
    def test_status(self):
        status()
        self.assertEqual(sys.stdout.getvalue().strip(), "Slot No.\tRegistration No.\tColor\n2\tKA-01-HH-1234\tWhite\n4\tKA-01-HH-9999\tWhite")

    @patch.dict(R_NO_COLOR, {"White": ["KA-01-HH-1234", "KA-01-HH-9999"]}, clear=True)
    def test_registration_numbers_for_cars_with_colour(self):
        color = "White"
        registration_numbers_for_cars_with_colour(color)
        self.assertEqual(sys.stdout.getvalue().strip(), "KA-01-HH-1234, KA-01-HH-9999")

    @patch.dict(SLOT_NO_COLOR, {"White": [2, 4]}, clear=True)
    def test_slot_numbers_for_cars_with_colour(self):
        color = "White"
        slot_numbers_for_cars_with_colour(color)
        self.assertEqual(sys.stdout.getvalue().strip(), "2, 4")

    @patch.dict(SLOT_NO_REG, {"KA-01-HH-1234": 2, "KA-01-HH-9999": 4}, clear=True)
    def test_slot_number_for_registration_number_exists(self):
        registration_number = "KA-01-HH-9999"
        slot_number_for_registration_number(registration_number)
        self.assertEqual(sys.stdout.getvalue().strip(), "4")

    @patch.dict(SLOT_NO_REG, {"KA-01-HH-1234": 2, "KA-01-HH-9999": 4}, clear=True)
    def test_slot_number_for_registration_number_does_not_exist(self):
        registration_number = "KA-01-HH-1729"
        slot_number_for_registration_number(registration_number)
        self.assertEqual(sys.stdout.getvalue().strip(), "Not found")


if __name__ == "__main__":
    unittest.main()
