import sys
import unittest

from io import StringIO
from unittest.mock import patch

from parking_lot.app import ParkingLot
from parking_lot.src.app import (LOT,
                                 DATA,
                                 R_NO_COLOR,
                                 SLOT_NO_REG,
                                 SLOT_NO_COLOR)


class MainAppTest(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def create(self):
        return ParkingLot()

    def test_do_create_parking_lot(self):
        cli = self.create()
        cli.onecmd("create_parking_lot 8")
        self.assertEqual(sys.stdout.getvalue().strip(), "Created a parking lot with 8 slots")

    @patch.dict(LOT, {1: True, 2: False, 3: False, 4: False}, clear=True)
    @patch.dict(DATA, {}, clear=True)
    @patch.dict(R_NO_COLOR, {}, clear=True)
    @patch.dict(SLOT_NO_REG, {}, clear=True)
    @patch.dict(SLOT_NO_COLOR, {}, clear=True)
    def test_do_park(self):
        cli = self.create()
        cli.onecmd("park KA-01-HH-1234 White")
        self.assertEqual(sys.stdout.getvalue().strip(), "Allocated slot number: 2")

    @patch.dict(LOT, {1: False, 2: True, 3: False, 4: True}, clear=True)
    @patch.dict(DATA, {2: {'registration_number': "KA-01-HH-1234", 'color': "White"}, 4: {'registration_number': "KA-01-HH-9999", 'color': "White"}}, clear=True)
    @patch.dict(R_NO_COLOR, {"White": ["KA-01-HH-1234", "KA-01-HH-9999"]}, clear=True)
    @patch.dict(SLOT_NO_REG, {"KA-01-HH-1234": 2, "KA-01-HH-9999": 4}, clear=True)
    @patch.dict(SLOT_NO_COLOR, {"White": [2, 4]}, clear=True)
    def test_do_leave(self):
        cli = self.create()
        cli.onecmd("leave 4")
        self.assertEqual(sys.stdout.getvalue().strip(), "Slot number 4 is free")

    @patch.dict(LOT, {1: False, 2: True, 3: False, 4: True}, clear=True)
    @patch.dict(DATA, {2: {'registration_number': "KA-01-HH-1234", 'color': "White"}, 4: {'registration_number': "KA-01-HH-9999", 'color': "White"}}, clear=True)
    @patch.dict(R_NO_COLOR, {"White": ["KA-01-HH-1234", "KA-01-HH-9999"]}, clear=True)
    @patch.dict(SLOT_NO_REG, {"KA-01-HH-1234": 2, "KA-01-HH-9999": 4}, clear=True)
    @patch.dict(SLOT_NO_COLOR, {"White": [2, 4]}, clear=True)
    def test_status(self):
        cli = self.create()
        cli.onecmd("status")
        self.assertEqual(sys.stdout.getvalue().strip(), "Slot No.\tRegistration No.\tColor\n2\tKA-01-HH-1234\tWhite\n4\tKA-01-HH-9999\tWhite")

if __name__ == "__main__":
    unittest.main()
