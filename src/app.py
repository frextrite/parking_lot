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

    if slot == 0:
        print("Sorry, parking lot is full")
        return

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


def leave(slot):
    if LOT[slot] is True:
        LOT[slot] = False

    registration_number = DATA[slot]['registration_number']
    color = DATA[slot]['color']

    if color in R_NO_COLOR:
        R_NO_COLOR[color].remove(registration_number)

    if registration_number in SLOT_NO_REG:
        SLOT_NO_REG.pop(registration_number)

    if color in SLOT_NO_COLOR:
        SLOT_NO_COLOR[color].remove(slot)

    print(f"Slot number {slot} is free")


def status():
    print("Slot No.\tRegistration No.\tColor")
    for slot in LOT:
        if LOT[slot] is True:
            print(f"{slot}\t{DATA[slot]['registration_number']}\t{DATA[slot]['color']}")


def registration_numbers_for_cars_with_colour(color):
    string = ""
    if color in R_NO_COLOR:
        for reg in R_NO_COLOR[color]:
            string += reg + ", "

    string = string[:-2]
    print(string)


def slot_numbers_for_cars_with_colour(color):
    string = ""
    if color in SLOT_NO_COLOR:
        for slot in SLOT_NO_COLOR[color]:
            string += str(slot) + ", "

    string = string[:-2]
    print(string)


def slot_number_for_registration_number(registration_number):
    string = ""
    if registration_number in SLOT_NO_REG:
        string = str(SLOT_NO_REG[registration_number])
    else:
        string = "Not found"

    print(string)
