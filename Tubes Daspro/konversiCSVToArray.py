def GameCSVToArray():
    global dataGame
    f = open("FileCSV/game.csv", "r")
    lines = f.readlines()
    f.close()

    dataGame = []

    for line in lines:
        n = 0
        line_data = ['']
        for char in line:
            if char == ';':
                line_data += ['']
                n += 1
            elif char != '\n':
                line_data[n] += char

        dataGame += [line_data]

    return dataGame

def UserCSVToArray():
    global dataUser
    f = open("FileCSV/user.csv", "r")
    lines = f.readlines()
    f.close()

    dataUser = []

    for line in lines:
        n = 0
        line_data = ['']
        for char in line:
            if char == ';':
                line_data += ['']
                n += 1
            elif char != '\n':
                line_data[n] += char

        dataUser += [line_data]

    return dataUser

def riwayatCSVToArray():
    global dataRiwayat
    f = open("FileCSV/user.csv", "r")
    lines = f.readlines()
    f.close()

    dataRiwayat = []

    for line in lines:
        n = 0
        line_data = ['']
        for char in line:
            if char == ';':
                line_data += ['']
                n += 1
            elif char != '\n':
                line_data[n] += char

        dataRiwayat += [line_data]

    return dataRiwayat

def InventoryCSVToArray():
    global Inventory
    f = open("FileCSV/inventory.csv", "r")
    lines = f.readlines()
    f.close()

    dataInventory = []

    for line in lines:
        n = 0
        line_data = ['']
        for char in line:
            if char == ';':
                line_data += ['']
                n += 1
            elif char != '\n':
                line_data[n] += char

        dataInventory += [line_data]

    return dataInventory
