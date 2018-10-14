LOT = dict()
R_NO_COLOR = dict()
SLOT_NO_REG = dict()
SLOT_NO_COLOR = dict()


def create_parking_lot(n):
    for i in range(n):
        LOT[i + 1] = False
    print(f"Created a parking lot with {n} slots")


def park(registration_number, color):
    pass
