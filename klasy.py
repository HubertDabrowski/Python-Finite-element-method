class node:
    x = 0.0
    y = 0.0
    t = 0
    BC = 0

class element:
    id = []

    def __init__(self):
        id = [0,0,0,0]


class grid:
    numberOfNd = 0
    numberOfEl = 0
    ND = [] #tablica obiektow node
    EL = [] #tablica obiektow element


class globalData:
    simTime = 0
    simStepTime = 0
    conductivity = 0
    alfa = 0
    tot = 0
    initTemp = 0
    density = 0
    specificHeat = 0