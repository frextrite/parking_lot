LOT = dict()
DATA = dict()
R_NO_COLOR = dict()
SLOT_NO_REG = dict()
SLOT_NO_COLOR = dict()


def create_parking_lot(n):
    for i in range(n):
        LOT[i + 1] = False
    print(f"Created a parking lot with {n} slots")


def park(registration_number, color):
    slot = 0
    for i in LOT.keys():
        if LOT[i] is False:
            LOT[i] = True
            slot = i
            break

    DATA[slot] = dict(registration_number=registration_number, color=color)

    if color not in R_NO_COLOR:
        R_NO_COLOR[color] = [registration_number]
    else:
        R_NO_COLOR[color].append(registration_number)

    if registration_number not in SLOT_NO_REG:
        SLOT_NO_REG[registration_number] = slot

    if color not in SLOT_NO_COLOR:
        SLOT_NO_COLOR[color] = [slot]
    else:
        SLOT_NO_COLOR[color].append(slot)

    print(f"Allocated slot number: {slot}")
