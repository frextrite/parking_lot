lot = dict()


def create_parking_lot(n):
    for i in range(n):
        lot[i + 1] = False
    print(f"Created a parking lot with {n} slots")
