import sys
import unittest

from io import StringIO
from unittest.mock import MagicMock
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

    @patch('parking_lot.app.create_parking_lot')
    def test_do_create_parking_lot(self, mock_create_parking_lot):
        cli = self.create()
        cli.onecmd("create_parking_lot 8")
        mock_create_parking_lot.assert_called_once_with(8)

    @patch('parking_lot.app.park')
    def test_do_park(self, mock_park):
        cli = self.create()
        cli.onecmd("park KA-01-HH-1234 White")
        mock_park.assert_called_once_with("KA-01-HH-1234", "White")

    @patch('parking_lot.app.leave')
    def test_do_leave(self, mock_leave):
        cli = self.create()
        cli.onecmd("leave 4")
        mock_leave.assert_called_once_with(4)

    @patch('parking_lot.app.status')
    def test_do_status(self, mock_status):
        cli = self.create()
        cli.onecmd("status")
        mock_status.assert_called_once()

    @patch('parking_lot.app.slot_numbers_for_cars_with_colour')
    def test_do_slot_numbers_for_cars_with_colour(self, mock_slot_numbers_for_cars_with_colour):
        cli = self.create()
        cli.onecmd("slot_numbers_for_cars_with_colour White")
        mock_slot_numbers_for_cars_with_colour.assert_called_once_with("White")

    @patch('parking_lot.app.slot_number_for_registration_number_exists')
    def test_do_slot_number_for_registration_number_exists(self, mock_slot_number_for_registration_number_exists):
        cli = self.create()
        cli.onecmd("slot_number_for_registration_number_exists KA-01-HH-1234")
        mock_slot_number_for_registration_number_exists.assert_called_once_with("KA-01-HH-1234")


if __name__ == "__main__":
    unittest.main()
