import sys
import unittest

from io import StringIO

from parking_lot.app import ParkingLot


class MainAppTest(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def create(self):
        return ParkingLot()

    def test_do_create_parking_lot(self):
        cli = self.create()
        cli.onecmd("create_parking_lot 8")
        self.assertEqual(sys.stdout.getvalue().strip(), "Created a parking lot with 8 slots")

    def test_do_park(self):
        cli = self.create()
        cli.onecmd("park KA-01-HH-1234")
        self.assertEqual(sys.stdout.getvalue().strip(), "Allocated slot number: 2")


if __name__ == "__main__":
    unittest.main()
