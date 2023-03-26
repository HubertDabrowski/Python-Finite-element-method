import load
import math
import klasy as kl
import jakobian as jkb
import agregation as ag
import wektor as wk
import matrixC as mC
import numpy as np

#obiekty do wczytania
globalData = kl.globalData()
grid = kl.grid()
path = 'Test2_4_4_MixGrid.txt'
#
#'Test3_31_31_kwadrat.txt'
#'test.txt'
#'Test1_4_4.txt'

#załadowanie z pliku
load.loadFile(globalData, grid, path)

#dane
iloPktSchemat = 2

if(iloPktSchemat == 2):
    punktyCalkowania =  [-(1/math.sqrt(3)),(1/math.sqrt(3))]
    waga = [1, 1]
elif(iloPktSchemat == 3):
    punktyCalkowania = [-math.sqrt(3 / 5), 0, math.sqrt(3 / 5)]
    waga = [(5 / 9), (8 / 9), (5 / 9)]
elif(iloPktSchemat == 4):
    punktyCalkowania = [-0.861136,-0.339981,0.339981,0.861136]
    waga = [0.347855, 0.652145, 0.652145, 0.347855]


#tu sie zaczyna wyliczanie macierzy/wektorów
tablicaElem = jkb.elemKsiEta(punktyCalkowania)
tablicaElem.printArr(iloPktSchemat)                             #wypisuje macierz dN/d ksi i eta
print('')

myJakobianArr = [jkb.jakobian() for i in range(grid.numberOfEl)]            #trzyma jakobiany dla każdego elementu
matrixH = [jkb.macierzH() for i in range(grid.numberOfEl)]                  #trzyma macierze H dla kalżego elementu siatki
matrixC = [mC.macierzC(iloPktSchemat,punktyCalkowania) for i in range(grid.numberOfEl)]
myWektorPArr = [[0,0,0,0] for i in range(grid.numberOfEl)]           #tablica z wektorami p dla każdego elementu
tablicaElem2 = [jkb.elemXY() for i in range(grid.numberOfEl)]
print(myWektorPArr)
print("arrayC len:"+ str(len(matrixC)))
for j in range(grid.numberOfEl):
    myJakobianArr[j]= jkb.obliczJakobian(j,grid,iloPktSchemat,tablicaElem) #nr elementu podajemy tak jak na obrazku było
    # myJakobianArr[j].showJakobian(iloPktSchemat)
    myJakobianArr[j] = jkb.obliczPochXY(myJakobianArr[j],iloPktSchemat)
    # myJakobianArr[j].showJakobian(iloPktSchemat)
    print('')

    tablicaElem2[j].myInitXY(punktyCalkowania,tablicaElem,myJakobianArr[j])#to ten moment przed liczeniem macierzy H z prezentacji
    tablicaElem2[j].printArr(iloPktSchemat)                   #wypisuje macierz dN/d x i y
    print('')

    detJ = []
    detJ = jkb.initDetJ(myJakobianArr[j],iloPktSchemat)
    print(detJ[0])
    print(detJ[1])
    print(detJ[2])
    print(detJ[3])
    print('')

    if(iloPktSchemat  == 2):                                #tworzenie tyle obiektów ile pkt całkowania
        arrayH = [jkb.macierzH() for i in range(4)]
        arrayC = [mC.macierzC(iloPktSchemat,punktyCalkowania) for i in range(4)]

        for i in range(4):
            arrayH[i].matrix = jkb.partialH(tablicaElem2[j],i+1,globalData.conductivity,detJ,iloPktSchemat)
            arrayC[i].matrix = mC.partialC(matrixC[j].wartoscN[i],globalData.density,globalData.specificHeat,detJ,i+1,iloPktSchemat)
            # print("macierz dla punktu w elemencie"+str(j+1))
            # arrayH[i].printPartArr(i+1)

    if(iloPktSchemat  == 3):
        arrayH = [jkb.macierzH() for i in range(9)]
        arrayC = [mC.macierzC(iloPktSchemat, punktyCalkowania) for i in range(9)]
        #print(arrayH[0])
        for i in range(9):
            arrayH[i].matrix = jkb.partialH(tablicaElem2[j],i+1,globalData.conductivity,detJ,iloPktSchemat)
            arrayC[i].matrix = mC.partialC(matrixC[j].wartoscN[i], globalData.density, globalData.specificHeat, detJ,i+1,iloPktSchemat)
            #arrayH[i].printPartArr(i+1)

    if(iloPktSchemat  == 4):
        arrayH = [jkb.macierzH() for i in range(16)]
        arrayC = [mC.macierzC(iloPktSchemat, punktyCalkowania) for i in range(16)]
        #print(arrayH[0])
        for i in range(16):
            arrayH[i].matrix = jkb.partialH(tablicaElem2[j],i+1,globalData.conductivity,detJ,iloPktSchemat)
            arrayC[i].matrix = mC.partialC(matrixC[j].wartoscN[i], globalData.density, globalData.specificHeat, detJ, i + 1,iloPktSchemat)
            #arrayH[i].printPartArr(i+1)
    # print('macierz H przed' + str(j + 1))
    # matrixH[j].printArr(j)
    matrixH[j].margeH(arrayH,waga,iloPktSchemat)    #złączenie w całość z wszystkich macierzy z pkt całkowania
    print('macierz H'+ str(j+1))
    matrixH[j].printArr(j)

    matrixC[j].margeC(arrayC, waga, iloPktSchemat)  # złączenie w całość z wszystkich macierzy z pkt całkowania
    # print('macierz C' + str(j + 1))
    # matrixC[j].printArr(j)

    nodeNumbers = ag.getNdNumbers(j,grid)
    if(grid.ND[nodeNumbers[0]-1].BC == 1 and grid.ND[nodeNumbers[1]-1].BC == 1):                    #sprawdzenie czy ściana ma warunek brzegowy
        myBok1 = jkb.bok1(iloPktSchemat)
        myMatrixHbc1 = jkb.partialHbc(myBok1, iloPktSchemat, globalData.alfa, waga,grid.ND[nodeNumbers[0]-1],grid.ND[nodeNumbers[1]-1])
        myWektorP1 =  wk.partialP(myBok1, iloPktSchemat, globalData.alfa, waga,grid.ND[nodeNumbers[0]-1],grid.ND[nodeNumbers[1]-1],globalData.tot)
    else:
        myMatrixHbc1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        myWektorP1 = [0,0,0,0]

    if (grid.ND[nodeNumbers[1]-1].BC == 1 and grid.ND[nodeNumbers[2]-1].BC == 1):
        myBok2 = jkb.bok2(iloPktSchemat)
        myMatrixHbc2 = jkb.partialHbc(myBok2, iloPktSchemat, globalData.alfa, waga,grid.ND[nodeNumbers[1]-1],grid.ND[nodeNumbers[2]-1])
        myWektorP2 = wk.partialP(myBok2, iloPktSchemat, globalData.alfa, waga, grid.ND[nodeNumbers[1] - 1],grid.ND[nodeNumbers[2] - 1],globalData.tot)
    else:
        myMatrixHbc2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        myWektorP2 = [0, 0, 0, 0]

    if (grid.ND[nodeNumbers[2]-1].BC == 1 and grid.ND[nodeNumbers[3]-1].BC == 1):
        myBok3 = jkb.bok3(iloPktSchemat)
        myMatrixHbc3 = jkb.partialHbc(myBok3, iloPktSchemat, globalData.alfa, waga,grid.ND[nodeNumbers[2]-1],grid.ND[nodeNumbers[3]-1])
        myWektorP3 = wk.partialP(myBok3, iloPktSchemat, globalData.alfa, waga, grid.ND[nodeNumbers[2] - 1],grid.ND[nodeNumbers[3] - 1],globalData.tot)
    else:
        myMatrixHbc3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        myWektorP3 = [0, 0, 0, 0]

    if (grid.ND[nodeNumbers[3]-1].BC == 1 and grid.ND[nodeNumbers[0]-1].BC == 1):
        myBok4 = jkb.bok4(iloPktSchemat)
        myMatrixHbc4 = jkb.partialHbc(myBok4, iloPktSchemat, globalData.alfa, waga,grid.ND[nodeNumbers[3]-1],grid.ND[nodeNumbers[0]-1])
        myWektorP4 = wk.partialP(myBok4, iloPktSchemat, globalData.alfa, waga, grid.ND[nodeNumbers[3] - 1],grid.ND[nodeNumbers[0] - 1],globalData.tot)
    else:
        myMatrixHbc4 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        myWektorP4 = [0, 0, 0, 0]

    finalHbc=jkb.margeHbc(myMatrixHbc1,myMatrixHbc2,myMatrixHbc3,myMatrixHbc4)
    #złączenie macierzy hbc ścian w jedną
    finalP = wk.margeP(myWektorP1,myWektorP2,myWektorP3,myWektorP4)
    print('hbc element'+ str(j+1))
    jkb.printHbc(finalHbc)                                                              #wypisanie lokalne dla konkretnego elementu macierzy hbc

    print('przed')
    wk.printP(myWektorPArr[j])
    myWektorPArr[j]=(finalP)
    print('wektor p element'+ str(j+1))
    wk.printP(myWektorPArr[j])


    print('macierz HBC' + str(j + 1))
    matrixH[j].printArr(j)

    for d in range(4):
        for k in range(4):
            matrixH[j].matrix[d][k]+=finalHbc[d][k]                              #dodanie hbc do macierzu h konkretnego elementu
            #finalHbc[d][k]=0


#agregacje tu sie zaczynają
myAgrHbc = ag.agregation()
myAgrHbc.myInit(grid.numberOfNd)
ag.agregateArr(myAgrHbc,matrixH,grid)
print('macierzHbc:')
myAgrHbc.showArr(grid.numberOfNd)
print('')

wektorP = ag.agregateWektorP(myWektorPArr,grid)                             #zagregowane wektory p
print('wektorP:')
ag.showArr(wektorP,grid.numberOfNd)

myAgrC = ag.agregationC()
myAgrC.myInit(grid.numberOfNd)
ag.agregateArr(myAgrC,matrixC,grid)
print('macierzC:')
myAgrC.showArr(grid.numberOfNd)


#tu sie zaczyna obliczanie równania
HplusC = []
Tzero = []

print()
for i in range(grid.numberOfNd):
    HplusC.append([])
    for j in range(grid.numberOfNd):
        myAgrC.agrArr[i][j] = myAgrC.agrArr[i][j]* (1/globalData.simStepTime)
        HplusC[i].append(0)

for i in range(grid.numberOfNd):    #dodanie Hbc i C
    Tzero.append(globalData.initTemp)
    for j in range(grid.numberOfNd):
        HplusC[i][j] = myAgrC.agrArr[i][j] + myAgrHbc.agrArr[i][j]

C_razyT = np.matmul(myAgrC.agrArr,Tzero)
PplusC = []
for i in range(grid.numberOfNd):
    PplusC.append(C_razyT[i]+wektorP[i])


t=0
for i in range(int(globalData.simTime/globalData.simStepTime)):
    t+=globalData.simStepTime
    Tjeden = np.linalg.solve(HplusC, PplusC)
    Tzero = Tjeden;

    C_razyT = np.matmul(myAgrC.agrArr, Tzero)
    for j in range(grid.numberOfNd):
        PplusC[j]=(C_razyT[j] + wektorP[j])

    print('t: '+str(t) + "  min temp: " + str(round(np.min(Tjeden),2)) + "  max temp: " + str(np.max(round(max(Tjeden),2))))
