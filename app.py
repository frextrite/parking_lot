import cmd

from parking_lot.src.app import (create_parking_lot, 
                                 park,
                                 leave,
                                 status,
                                 registration_numbers_for_cars_with_colour,
                                 slot_numbers_for_cars_with_colour,
                                 slot_number_for_registration_number_exists)
from parking_lot.src.app import DATA, LOT, R_NO_COLOR, SLOT_NO_REG, SLOT_NO_COLOR


class ParkingLot(cmd.Cmd):
    def parse_args(self, args):
        return args.split(' ')

    def do_create_parking_lot(self, args):
        args_list = self.parse_args(args)
        slots = int(args_list[0])
        create_parking_lot(slots)
