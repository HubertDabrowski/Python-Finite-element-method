import klasy as klasa

def loadFile(globalData, grid, path):
    # DANE
    file = open(path, 'r')  # r - read
    wordsArray = []

    # PIERWSZA CZ PLIKU
    for i in range(10):
        line = file.readline()  # czyta tekst linijkami
        temp = line.split()
        wordsArray.append(temp[len(temp) - 1])
        # print(wordsArray[len(wordsArray)-1])

    globalData.simTime = int(wordsArray[0])
    globalData.simStepTime = int(wordsArray[1])
    globalData.conductivity = int(wordsArray[2])
    globalData.alfa = int(wordsArray[3])
    globalData.tot = int(wordsArray[4])
    globalData.initTemp = int(wordsArray[5])
    globalData.density = int(wordsArray[6])
    globalData.specificHeat = int(wordsArray[7])
    grid.numberOfNd = int(wordsArray[8])
    grid.numberOfEl = int(wordsArray[9])
    #print(grid.numberOfNd)
    #print(grid.numberOfEl)

    # DRUGA CZ PLIKU

    wordsArray.clear()
    line = file.readline()

    grid.ND = [klasa.node() for i in range(grid.numberOfNd)]  # dodanie obiektów do listy

    for nd in range(grid.numberOfNd):
        wordsArray.clear()
        line = file.readline()
        temp = line.split()
        noComma = temp[len(temp) - 2].replace(',', '')  # usuniecie przecinka na koncu
        wordsArray.append(noComma)
        wordsArray.append(temp[len(temp) - 1])

        # print(float(wordsArray[0]))
        # print(float(wordsArray[1]))
        grid.ND[nd].x = float(wordsArray[0])       # wstawienie do tablicy z elementami ich id pobranych z pliku
        grid.ND[nd].y = float(wordsArray[1])


    # TRZECIA CZ PLIKU

    wordsArray.clear()
    line = file.readline()

    grid.EL = [klasa.element() for i in range(grid.numberOfEl)] #dodanie obiektów do listy
    j=0

    for el in range(grid.numberOfEl):
        wordsArray.clear()
        line = file.readline()
        temp = line.split()
        noComma = temp[len(temp) - 4].replace(',', '')  # usuniecie przecinka na koncu
        wordsArray.append(noComma)
        noComma = temp[len(temp) - 3].replace(',', '')  # usuniecie przecinka na koncu
        wordsArray.append(noComma)
        noComma = temp[len(temp) - 2].replace(',', '')  # usuniecie przecinka na koncu
        wordsArray.append(noComma)
        wordsArray.append(temp[len(temp) - 1])
        #print(wordsArray)

        grid.EL[j].id = [int (x) for x in wordsArray] #wstawienie do tablicy z elementami ich id pobranych z pliku
        j+=1


    # CZWARTA CZ PLIKU
    wordsArray.clear()
    line = file.readline()
    line = file.readline()
    temp = line.split()

    for i in range(len(temp)):
        noComma = temp[i].replace(',', '')  # usuniecie przecinka na koncu
        grid.ND[int(noComma) - 1].BC = 1
