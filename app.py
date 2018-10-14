import cmd

from src.app import (create_parking_lot, 
                     park,
                     leave,
                     status,
                     registration_numbers_for_cars_with_colour,
                     slot_numbers_for_cars_with_colour,
                     slot_number_for_registration_number)
from src.app import DATA, LOT, R_NO_COLOR, SLOT_NO_REG, SLOT_NO_COLOR


class ParkingLot(cmd.Cmd):
    def parse_args(self, args):
        return args.split(' ')

    def do_create_parking_lot(self, args):
        args_list = self.parse_args(args)
        slots = int(args_list[0])
        create_parking_lot(slots)

    def do_park(self, args):
        args_list = self.parse_args(args)
        registration_number = args_list[0]
        color = args_list[1]
        park(registration_number, color)

    def do_leave(self, args):
        args_list = self.parse_args(args)
        slot = int(args_list[0])
        leave(slot)

    def do_status(self, args):
        status()

    def do_slot_numbers_for_cars_with_colour(self, args):
        args_list = self.parse_args(args)
        color = args_list[0]
        slot_numbers_for_cars_with_colour(color)

    def do_slot_number_for_registration_number(self, args):
        args_list = self.parse_args(args)
        registration_number = args_list[0]
        slot_number_for_registration_number(registration_number)

    def do_registration_numbers_for_cars_with_colour(self, args):
        args_list = self.parse_args(args)
        color = args_list[0]
        registration_numbers_for_cars_with_colour(color)

    def do_exit(self, args):
        return True


if __name__ == "__main__":
    import sys
    try:
        input = open(sys.argv[1], 'rt')
        pl = ParkingLot(stdin=input)
        pl.use_rawinput = False
        pl.prompt = ''
        pl.cmdloop()
    except IndexError:
        pl = ParkingLot()
        pl.prompt = '> '
        pl.cmdloop()
