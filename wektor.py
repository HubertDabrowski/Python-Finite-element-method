import math

class wektor:
    P = []

    def __init__(self, grid):
        for i in range(grid.numberOfNd):
            self.P.append(0)


def partialP(bok, ilePktC, alfa, wagi, pk1, pk2,tempOtoczenia):  # liczby macierz hbc dla jednego boku alfa
    wektorP1 = [0, 0, 0, 0]
    wektorP2 = [0, 0, 0, 0]
    wektorP3 = [0, 0, 0, 0]
    wektorP4 = [0, 0, 0, 0]
    wektorP = [0, 0, 0, 0]

    detJ = (math.sqrt(math.pow((pk2.x - pk1.x), 2) + math.pow((pk2.y - pk1.y), 2)) / 2)

    if ilePktC == 2:
        for i in range(4):
            wektorP1[i]=(wagi[0] * (bok.wartoscN[0][i]))
            wektorP2[i]=(wagi[1] * (bok.wartoscN[1][i]))

        for i in range(4):
            wektorP[i]=(detJ * alfa * (wektorP1[i] + wektorP2[i])*tempOtoczenia)

    if ilePktC == 3:
        for i in range(4):
            wektorP1[i]=(wagi[0] * (bok.wartoscN[0][i]))
            wektorP2[i]=(wagi[1] * (bok.wartoscN[1][i]))
            wektorP3[i]=(wagi[2] * (bok.wartoscN[2][i]))
        for i in range(4):
            wektorP[i]=(detJ * alfa * (wektorP1[i] + wektorP2[i]+ wektorP3[i]) * tempOtoczenia)

    if ilePktC == 4:
        for i in range(4):
            wektorP1[i]=(wagi[0] * (bok.wartoscN[0][i]))
            wektorP2[i]=(wagi[1] * (bok.wartoscN[1][i]))
            wektorP3[i]=(wagi[2] * (bok.wartoscN[2][i]))
            wektorP4[i]=(wagi[3] * (bok.wartoscN[3][i]))
        for i in range(4):
            wektorP[i]=(detJ * alfa * (wektorP1[i] + wektorP2[i]+wektorP3[i]+wektorP4[i]) * tempOtoczenia)

    return wektorP


def margeP(m1, m2, m3, m4):  # złacenie macierzy dla kazdego boku do jedenej dla calego elementu
    finalWektorP = [0,0,0,0]
    for i in range(4):
        finalWektorP[i]=(m1[i] + m2[i] + m3[i] + m4[i])
    return finalWektorP

def printP(p):
    for i in range(4):
        print(p[i])
    print()
