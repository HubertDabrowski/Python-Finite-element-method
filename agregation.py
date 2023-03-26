class agregation:
    agrArr = []

    def myInit(self, numberOfNd):
        for i in range(numberOfNd):
            self.agrArr.append([])
            for j in range(numberOfNd):
                self.agrArr[i].append(round(0.0,2))


    def showArr(self, numberOfNd):
        for i in range(numberOfNd):
                print(self.agrArr[i])

class agregationC:
    agrArr = []

    def myInit(self, numberOfNd):
        for i in range(numberOfNd):
            self.agrArr.append([])
            for j in range(numberOfNd):
                self.agrArr[i].append(round(0.0,2))


    def showArr(self, numberOfNd):
        for i in range(numberOfNd):
                print(self.agrArr[i])

def agregateArr(agr, arrH, grid):
    for i in range(grid.numberOfEl):
        nodesNumbers = []
        nodesNumbers = getNdNumbers(i,grid)
        #print(nodesNumbers)
        for j in range(4): #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            for k in range(4):
                agr.agrArr[nodesNumbers[j]-1][nodesNumbers[k]-1] += round(arrH[i].matrix[j][k],6)


def getNdNumbers(nrElementu, grid):
    tempNode=[0,0,0,0]
    tempNode[0] = grid.EL[nrElementu].id[0] #1265
    tempNode[1] = grid.EL[nrElementu].id[1]
    tempNode[2] = grid.EL[nrElementu].id[2] #1,2,3,4 = 6,5,1,2
    tempNode[3] = grid.EL[nrElementu].id[3]
    return tempNode

def agregateWektorP(arrP,grid): #nie dziala
    agrWektorP = []
    for x in range(grid.numberOfNd):
        agrWektorP.append(0)

    for i in range(grid.numberOfEl):
        nodesNumbers = []
        nodesNumbers = getNdNumbers(i, grid)
        # print(nodesNumbers)
        for j in range(4):
                agrWektorP[nodesNumbers[j] - 1] += arrP[i][j]

    return agrWektorP

def showArr(arr,numberOfNd):
    for i in range(numberOfNd):
        print(arr[i])
    print()