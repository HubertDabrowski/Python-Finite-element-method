import math
import klasy as kl
import agregation as ag

class elemKsiEta:
    arrEta = [[],[],[],[]]
    arrKsi = [[],[],[],[]]

    def __init__(self, pktCalkowania):
        if len(pktCalkowania) == 2: #jak 2 pkt całkowania to tworzy sie 4kwadraty
            for i in range(4): #wersy - wywołanie 4 funkcji pochodnych dla konkretnego pkt calkowania
                if(i==0 or i==2):
                    self.arrEta[i].append(f1Eta(pktCalkowania[0]))  #dodawanie wynikow po kolei do pól
                    self.arrEta[i].append(f2Eta(pktCalkowania[0]))
                    self.arrEta[i].append(f4Eta(pktCalkowania[0]))
                    self.arrEta[i].append(f3Eta(pktCalkowania[0]))
                else:
                    self.arrEta[i].append(f1Eta(pktCalkowania[1]))
                    self.arrEta[i].append(f2Eta(pktCalkowania[1]))
                    self.arrEta[i].append(f4Eta(pktCalkowania[1]))
                    self.arrEta[i].append(f3Eta(pktCalkowania[1]))

                if(i<2):
                    self.arrKsi[i].append(f1Ksi(pktCalkowania[0]))
                    self.arrKsi[i].append(f2Ksi(pktCalkowania[0]))
                    self.arrKsi[i].append(f4Ksi(pktCalkowania[0]))
                    self.arrKsi[i].append(f3Ksi(pktCalkowania[0]))
                else:
                    self.arrKsi[i].append(f1Ksi(pktCalkowania[1]))
                    self.arrKsi[i].append(f2Ksi(pktCalkowania[1]))
                    self.arrKsi[i].append(f4Ksi(pktCalkowania[1]))
                    self.arrKsi[i].append(f3Ksi(pktCalkowania[1]))
        if len(pktCalkowania) == 3: #jak 3 pkt całkowania to tworzy sie 9kwadraty
            for i in range(5):
                self.arrEta.append([])
                self.arrKsi.append([])
            for i in range(9):
                if(i<3):
                    self.arrEta[i].append(f1Eta(pktCalkowania[0]))
                    self.arrEta[i].append(f3Eta(pktCalkowania[0]))
                    self.arrEta[i].append(f4Eta(pktCalkowania[0]))
                    self.arrEta[i].append(f2Eta(pktCalkowania[0]))
                elif(i>2 and i<6):
                    self.arrEta[i].append(f1Eta(pktCalkowania[1]))
                    self.arrEta[i].append(f3Eta(pktCalkowania[1]))
                    self.arrEta[i].append(f4Eta(pktCalkowania[1]))
                    self.arrEta[i].append(f2Eta(pktCalkowania[1]))
                else:
                    self.arrEta[i].append(f1Eta(pktCalkowania[2]))
                    self.arrEta[i].append(f3Eta(pktCalkowania[2]))
                    self.arrEta[i].append(f4Eta(pktCalkowania[2]))
                    self.arrEta[i].append(f2Eta(pktCalkowania[2]))

                if(i==0 or i==3 or i==6):
                    self.arrKsi[i].append(f1Ksi(pktCalkowania[0]))
                    self.arrKsi[i].append(f3Ksi(pktCalkowania[0]))
                    self.arrKsi[i].append(f4Ksi(pktCalkowania[0]))
                    self.arrKsi[i].append(f2Ksi(pktCalkowania[0]))
                elif(i==1 or i==4 or i==7):
                    self.arrKsi[i].append(f1Ksi(pktCalkowania[1]))
                    self.arrKsi[i].append(f3Ksi(pktCalkowania[1]))
                    self.arrKsi[i].append(f4Ksi(pktCalkowania[1]))
                    self.arrKsi[i].append(f2Ksi(pktCalkowania[1]))
                else:
                    self.arrKsi[i].append(f1Ksi(pktCalkowania[2]))
                    self.arrKsi[i].append(f3Ksi(pktCalkowania[2]))
                    self.arrKsi[i].append(f4Ksi(pktCalkowania[2]))
                    self.arrKsi[i].append(f2Ksi(pktCalkowania[2]))
        if len(pktCalkowania) == 4:  # jak 3 pkt całkowania to tworzy sie 9kwadraty
                    for i in range(12):
                        self.arrEta.append([])
                        self.arrKsi.append([])
                    for i in range(16):
                        if (i < 4):
                            self.arrEta[i].append(f1Eta(pktCalkowania[0]))
                            self.arrEta[i].append(f3Eta(pktCalkowania[0]))
                            self.arrEta[i].append(f4Eta(pktCalkowania[0]))
                            self.arrEta[i].append(f2Eta(pktCalkowania[0]))
                        elif (i > 3 and i < 8):
                            self.arrEta[i].append(f1Eta(pktCalkowania[1]))
                            self.arrEta[i].append(f3Eta(pktCalkowania[1]))
                            self.arrEta[i].append(f4Eta(pktCalkowania[1]))
                            self.arrEta[i].append(f2Eta(pktCalkowania[1]))
                        elif (i>7 and i< 12):
                            self.arrEta[i].append(f1Eta(pktCalkowania[2]))
                            self.arrEta[i].append(f3Eta(pktCalkowania[2]))
                            self.arrEta[i].append(f4Eta(pktCalkowania[2]))
                            self.arrEta[i].append(f2Eta(pktCalkowania[2]))
                        else:
                            self.arrEta[i].append(f1Eta(pktCalkowania[3]))
                            self.arrEta[i].append(f3Eta(pktCalkowania[3]))
                            self.arrEta[i].append(f4Eta(pktCalkowania[3]))
                            self.arrEta[i].append(f2Eta(pktCalkowania[3]))

                        if (i == 0 or i == 4 or i == 8 or i ==12):
                            self.arrKsi[i].append(f1Ksi(pktCalkowania[0]))
                            self.arrKsi[i].append(f3Ksi(pktCalkowania[0]))
                            self.arrKsi[i].append(f4Ksi(pktCalkowania[0]))
                            self.arrKsi[i].append(f2Ksi(pktCalkowania[0]))
                        elif (i == 1 or i == 5 or i == 9 or i == 13):
                            self.arrKsi[i].append(f1Ksi(pktCalkowania[1]))
                            self.arrKsi[i].append(f3Ksi(pktCalkowania[1]))
                            self.arrKsi[i].append(f4Ksi(pktCalkowania[1]))
                            self.arrKsi[i].append(f2Ksi(pktCalkowania[1]))
                        elif(i == 2 or i == 6 or i == 10 or i == 14):
                            self.arrKsi[i].append(f1Ksi(pktCalkowania[2]))
                            self.arrKsi[i].append(f3Ksi(pktCalkowania[2]))
                            self.arrKsi[i].append(f4Ksi(pktCalkowania[2]))
                            self.arrKsi[i].append(f2Ksi(pktCalkowania[2]))
                        else:
                            self.arrKsi[i].append(f1Ksi(pktCalkowania[3]))
                            self.arrKsi[i].append(f3Ksi(pktCalkowania[3]))
                            self.arrKsi[i].append(f4Ksi(pktCalkowania[3]))
                            self.arrKsi[i].append(f2Ksi(pktCalkowania[3]))

    def printArr(self, ilePkt):
        if ilePkt == 2:
            print('ETA:')
            for i in range(4):
                    print(str(self.arrEta[i][0]) + " " +str(self.arrEta[i][1])+" "+str(self.arrEta[i][2])+" "+str(self.arrEta[i][3]))
            print('')
            print('KSI:')
            for i in range(4):
                    print(str(self.arrKsi[i][0]) + " "+str(self.arrKsi[i][1])+" "+str(self.arrKsi[i][2])+" "+str(self.arrKsi[i][3]))

        if ilePkt == 3:
            print('ETA:')
            for i in range(9):
                    print(str(self.arrEta[i][0]) + " " +str(self.arrEta[i][1])+" "+str(self.arrEta[i][2])+" "+str(self.arrEta[i][3]))
            print('')
            print('KSI:')
            for i in range(9):
                    print(str(self.arrKsi[i][0]) + " "+str(self.arrKsi[i][1])+" "+str(self.arrKsi[i][2])+" "+str(self.arrKsi[i][3]))

        if ilePkt == 4:
            print('ETA:')
            for i in range(16):
                    print(str(self.arrEta[i][0]) + " " +str(self.arrEta[i][1])+" "+str(self.arrEta[i][2])+" "+str(self.arrEta[i][3]))
            print('')
            print('KSI:')
            for i in range(16):
                    print(str(self.arrKsi[i][0]) + " "+str(self.arrKsi[i][1])+" "+str(self.arrKsi[i][2])+" "+str(self.arrKsi[i][3]))

#funkcje pochodnych czastkowych dla 1/4(1+-x)(1+-y) do obliczeni elementu uniwersalnego dla H
def f1Eta(x):
    return (0.25)*(x-1)
def f2Eta(x):
    return (-0.25)*(x+1)
def f3Eta(x):
    return (0.25)*(1-x)
def f4Eta(x):
    return (0.25)*(x+1)
def f1Ksi(x):
    return  (0.25)*(x-1)
def f2Ksi(x):
    return (0.25)*(1-x)
def f3Ksi(x):
    return (-0.25)*(x+1)
def f4Ksi(x):
    return (0.25)*(x+1)

class elemXY:
    arrX = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    arrY = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def myInitXY(self, pktCalkowania, elemKsiEta, jkb):
        if len(pktCalkowania) == 2:
            for i in range(4):
                for j in range(4):
                    self.arrX[i][j] = ((jkb.yPoEta[i]*elemKsiEta.arrKsi[i][j])+(jkb.yPoKsi[i]*elemKsiEta.arrEta[i][j])) #dN1/dx
                    # self.arrX[i].append(jkb.yPoKsi[i]*elemKsiEta.arrKsi[i][1]+(-jkb.yPoEta[i])*elemKsiEta.arrEta[i][1]) #dN2/dx
                    # self.arrX[i].append(jkb.yPoKsi[i]*elemKsiEta.arrKsi[i][2]+(-jkb.yPoEta[i])*elemKsiEta.arrEta[i][2])#dN3/dx
                    # self.arrX[i].append(jkb.yPoKsi[i]*elemKsiEta.arrKsi[i][3]+(-jkb.yPoEta[i])*elemKsiEta.arrEta[i][3]) #dN4/dx

                    self.arrY[i][j] = (jkb.xPoEta[i] * elemKsiEta.arrKsi[i][j]) + (jkb.xPoKsi[i] * elemKsiEta.arrEta[i][j])
                    # self.arrY[i].append((-jkb.yPoKsi[i]) * elemKsiEta.arrKsi[i][1] + jkb.xPoKsi[i] * elemKsiEta.arrEta[i][1])
                    # self.arrY[i].append((-jkb.yPoKsi[i]) * elemKsiEta.arrKsi[i][2] + jkb.xPoKsi[i] * elemKsiEta.arrEta[i][2])
                    # self.arrY[i].append((-jkb.yPoKsi[i]) * elemKsiEta.arrKsi[i][3] + jkb.xPoKsi[i] * elemKsiEta.arrEta[i][3])  # ../dy

        elif len(pktCalkowania) == 3:
            for i in range(5):
                self.arrX.append([0,0,0,0])
                self.arrY.append([0,0,0,0])
            for i in range(9):
                for j in range(4):
                    self.arrX[i][j] = ((jkb.yPoEta[i] * elemKsiEta.arrKsi[i][j]) + (  jkb.yPoKsi[i] * elemKsiEta.arrEta[i][j]))  # dN1/dx
                    self.arrY[i][j] = (jkb.xPoEta[i] * elemKsiEta.arrKsi[i][j]) + (jkb.xPoKsi[i] * elemKsiEta.arrEta[i][j])

        elif len(pktCalkowania) == 4:
            for i in range(12):
                self.arrX.append([0,0,0,0])
                self.arrY.append([0,0,0,0])
            for i in range(16):
                for j in range(4):
                    self.arrX[i][j] = ((jkb.yPoEta[i] * elemKsiEta.arrKsi[i][j]) + (jkb.yPoKsi[i] * elemKsiEta.arrEta[i][j]))  # dN1/dx
                    self.arrY[i][j] = (jkb.xPoEta[i] * elemKsiEta.arrKsi[i][j]) + (jkb.xPoKsi[i] * elemKsiEta.arrEta[i][j])

    def printArr(self, ilePkt):
        if ilePkt == 2:
            print('x:')
            for i in range(4):
                    print(str(self.arrX[i][0]) + " " +str(self.arrX[i][1])+" "+str(self.arrX[i][2])+" "+str(self.arrX[i][3]))
            print('')
            print('Y:')
            for i in range(4):
                    print(str(self.arrY[i][0]) + " "+str(self.arrY[i][1])+" "+str(self.arrY[i][2])+" "+str(self.arrY[i][3]))

        elif ilePkt == 3:
            print('X:')
            for i in range(9):
                print(str(self.arrX[i][0]) + " " + str(self.arrX[i][1]) + " " + str(self.arrX[i][2]) + " " + str(
                    self.arrX[i][3]))
            print('')
            print('Y:')
            for i in range(9):
                print(str(self.arrY[i][0]) + " " + str(self.arrY[i][1]) + " " + str(self.arrY[i][2]) + " " + str(
                    self.arrY[i][3]))

        elif ilePkt == 4:
            print('X:')
            for i in range(16):
                print(str(self.arrX[i][0]) + " " + str(self.arrX[i][1]) + " " + str(self.arrX[i][2]) + " " + str(
                    self.arrX[i][3]))
            print('')
            print('Y:')
            for i in range(16):
                print(str(self.arrY[i][0]) + " " + str(self.arrY[i][1]) + " " + str(self.arrY[i][2]) + " " + str(
                    self.arrY[i][3]))

class jakobian:
    xPoKsi = []
    xPoEta = []
    yPoKsi = []
    yPoEta = []

    def showJakobian(self, ilePktCalkowania):
        if ilePktCalkowania == 2:
            for i in range(4):
                print("Punkt całkowania " + str(i+1))
                print(str(self.yPoEta[i]) + "  " + str(self.yPoKsi[i]))
                print(str(self.xPoEta[i]) + "  "+ str(self.xPoKsi[i]))

                print("")

        elif ilePktCalkowania == 3:
            for i in range(9):
                print("Punkt całkowania " + str(i+1))
                print(str(self.xPoKsi[i]) + "  " + str(self.yPoKsi[i]))
                print(str(self.xPoEta[i]) + "  "+ str(self.yPoEta[i]))
                print("")

        elif ilePktCalkowania == 4:
            for i in range(16):
                print("Punkt całkowania " + str(i+1))
                print(str(self.xPoKsi[i]) + "  " + str(self.yPoKsi[i]))
                print(str(self.xPoEta[i]) + "  "+ str(self.yPoEta[i]))
                print("")

def obliczJakobian(nrElementu, grid, ilePktCalkowania, elem):
    xPoKsi=[]   #obliczone po kolei dla 1pc, 2pc,3pc itd...
    xPoEta=[]
    yPoKsi=[]
    yPoEta=[]

    # tempXPoKsi=0.0 #beda trzymac sumy a potem ta suma bedzie wrzucana do tablicy
    # tempXPoEta=0.0
    # tempYPoKsi=0.0
    # tempYPoEta=0.0

    tempNode=[0,1,2,3] #tymczasowo wgrywamy nody z konkretnego elementu
    #for nodeNumber in grid.EL[nrElementu-1].id:
        #print(nodeNumber)
    tempNode[0]=(grid.ND[grid.EL[nrElementu].id[0]-1]) #1265
    tempNode[1]=(grid.ND[grid.EL[nrElementu].id[1]-1])
    tempNode[2]=(grid.ND[grid.EL[nrElementu].id[2]-1]) #1,2,3,4 = 6,5,1,2
    tempNode[3]=(grid.ND[grid.EL[nrElementu].id[3]-1])

    print("element number: " + str(nrElementu+1))
    print(str(grid.EL[nrElementu].id[0])+"  X = "+str(grid.ND[grid.EL[nrElementu].id[0]-1].x)+ " Y = "+str(grid.ND[grid.EL[nrElementu].id[0]-1].y))
    print(str(grid.EL[nrElementu].id[1])+"  X = "+str(grid.ND[grid.EL[nrElementu].id[1]-1].x)+ " Y = "+str(grid.ND[grid.EL[nrElementu].id[1]-1].y))
    print(str(grid.EL[nrElementu].id[2])+"  X = "+str(grid.ND[grid.EL[nrElementu].id[2]-1].x)+ " Y = "+str(grid.ND[grid.EL[nrElementu].id[2]-1].y))
    print(str(grid.EL[nrElementu].id[3])+"  X = "+str(grid.ND[grid.EL[nrElementu].id[3]-1].x)+ " Y = "+str(grid.ND[grid.EL[nrElementu].id[3]-1].y))
    print('')

    if(ilePktCalkowania == 2):
        xPoKsi = [0, 0, 0, 0]  # obliczone po kolei dla 1pc, 2pc,3pc itd...
        xPoEta = [0, 0, 0, 0]
        yPoKsi = [0, 0, 0, 0]
        yPoEta = [0, 0, 0, 0]
        for i in range(4):
            for j in range(4):                            #i-pc, j-po konkretnych polach z tego pc
                xPoKsi[i] += (tempNode[j].x * elem.arrKsi[i][j])  #sumujemy elementy z przygotowanej wcześniej tablicy przemnożone przez współrzędne
                xPoEta[i] += (tempNode[j].x * elem.arrEta[i][j])
                yPoKsi[i] += (tempNode[j].y * elem.arrKsi[i][j])
                yPoEta[i] += (tempNode[j].y * elem.arrEta[i][j])
            # xPoKsi[i] = (round(tempXPoKsi, 4))
            # xPoEta[i] = (round(tempXPoEta, 4))
            # yPoKsi[i] = (round(tempYPoKsi, 4))
            # yPoEta[i] = (round(tempYPoEta, 4))

    elif(ilePktCalkowania == 3):
        xPoKsi = [0, 0, 0,0,0,0,0,0,0]  # obliczone po kolei dla 1pc, 2pc,3pc itd...
        xPoEta = [0, 0, 0,0,0,0,0,0,0]
        yPoKsi = [0, 0, 0,0,0,0,0,0,0]
        yPoEta = [0, 0, 0,0,0,0,0,0,0]
        for i in range(9):
            for j in range(4):                           #i-pc, j-po konkretnych polach z tego pc
                xPoKsi[i] += (tempNode[j].x * elem.arrKsi[i][j])  # sumujemy elementy z przygotowanej wcześniej tablicy przemnożone przez współrzędne
                xPoEta[i] += (tempNode[j].x * elem.arrEta[i][j])
                yPoKsi[i] += (tempNode[j].y * elem.arrKsi[i][j])
                yPoEta[i] += (tempNode[j].y * elem.arrEta[i][j])

    elif (ilePktCalkowania == 4):
        xPoKsi = [0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0]  # obliczone po kolei dla 1pc, 2pc,3pc itd...
        xPoEta = [0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0]
        yPoKsi = [0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0]
        yPoEta = [0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in range(16):
            for j in range(4):
                xPoKsi[i] += (tempNode[j].x * elem.arrKsi[i][j])  # sumujemy elementy z przygotowanej wcześniej tablicy przemnożone przez współrzędne
                xPoEta[i] += (tempNode[j].x * elem.arrEta[i][j])
                yPoKsi[i] += (tempNode[j].y * elem.arrKsi[i][j])
                yPoEta[i] += (tempNode[j].y * elem.arrEta[i][j])

    jakobianTab = jakobian()
    jakobianTab.xPoKsi = xPoKsi
    jakobianTab.xPoEta = xPoEta
    jakobianTab.yPoKsi = yPoKsi
    jakobianTab.yPoEta = yPoEta

    return jakobianTab

def obliczPochXY(jkb, ilePktC):
    OdwDetJ = [0,0,0,0]

    if ilePktC == 2:
        for i in range(4):
            OdwDetJ[i]=(1/((jkb.xPoKsi[i] * jkb.yPoEta[i]) - (jkb.xPoEta[i] * jkb.yPoKsi[i])))
            jkb.yPoKsi[i] = -(jkb.yPoKsi[i]*OdwDetJ[i])
            jkb.yPoEta[i] = (jkb.yPoEta[i]*OdwDetJ[i])
            jkb.xPoKsi[i] = (jkb.xPoKsi[i]*OdwDetJ[i])
            jkb.xPoEta[i] = -(jkb.xPoEta[i]*OdwDetJ[i])


    elif ilePktC == 3:
        for i in range(5):
            OdwDetJ.append(0)
        for i in range(9):
            OdwDetJ[i] = (1 / ((jkb.xPoKsi[i] * jkb.yPoEta[i]) - (jkb.xPoEta[i] * jkb.yPoKsi[i])))
            jkb.yPoKsi[i] = -(jkb.yPoKsi[i]*OdwDetJ[i])
            jkb.yPoEta[i] = (jkb.yPoEta[i]*OdwDetJ[i])
            jkb.xPoKsi[i] = (jkb.xPoKsi[i]*OdwDetJ[i])
            jkb.xPoEta[i] = -(jkb.xPoEta[i]*OdwDetJ[i])

    elif ilePktC == 4:
        for i in range(12):
            OdwDetJ.append(0)
        for i in range(16):
            OdwDetJ[i] =(1/(round((jkb.xPoKsi[i] * jkb.yPoEta[i]) - (jkb.xPoEta[i] * jkb.yPoKsi[i]), 8)))
            jkb.yPoKsi[i] = -jkb.yPoKsi[i]*OdwDetJ[i]
            jkb.yPoEta[i] = jkb.yPoEta[i]*OdwDetJ[i]
            jkb.xPoKsi[i] = jkb.xPoKsi[i]*OdwDetJ[i]
            jkb.xPoEta[i] = -jkb.xPoEta[i]*OdwDetJ[i]

    return jkb

def initDetJ(jkb,ilePktC):
    list = []
    if ilePktC == 2:
        for i in range(4):
            list.append(1/(((jkb.xPoKsi[i] * jkb.yPoEta[i]) - (jkb.xPoEta[i] * jkb.yPoKsi[i]))))
    elif ilePktC == 3:
        for i in range(9):
            list.append(1/(((jkb.xPoKsi[i] * jkb.yPoEta[i]) - (jkb.xPoEta[i] * jkb.yPoKsi[i]))))
    elif ilePktC == 4:
        for i in range(16):
            list.append(1/(((jkb.xPoKsi[i] * jkb.yPoEta[i]) - (jkb.xPoEta[i] * jkb.yPoKsi[i]))))

    return list

class macierzH:
    matrix = [[],[],[],[]]

    def __init__(self):
        self.matrix=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def printPartArr(self, nrPktC):                         #wypisuje macierz H dla konkretnego punktu całkowania
            print(F'Macierz H pc{nrPktC}:')
            for i in range(4):
                print(str(self.matrix[i][0]) + " " +str(self.matrix[i][1])+" "+str(self.matrix[i][2])+" "+str(self.matrix[i][3]))
            print('')

    def printArr(self, nrEl):                                                                 #wypisuje końcową macierz H
        #print(f"Macierz dla elementu nr: {nrEl}:")
        for i in range(4):
            print(str(round(self.matrix[i][0],2)) + " " + str(round(self.matrix[i][1],2)) + " " + str(round(self.matrix[i][2],2)) + " " + str(round(self.matrix[i][3],2)))
        print('')

    def margeH(self,listaH,wagi,ilePktC):           #liczy macierz H finalną sumując i mnożąc przez wagi wszyskie macierze dla poszczególnych punktów całkowania
        if ilePktC == 2:
            for i in range(4):
                for j in range(4):
                    self.matrix[i][j]=( listaH[0].matrix[i][j]*wagi[0]*wagi[0]+listaH[1].matrix[i][j]*wagi[1]*wagi[0]+listaH[2].matrix[i][j]*wagi[0]*wagi[1]
                    +listaH[3].matrix[i][j]*wagi[1]*wagi[1])

        elif ilePktC == 3:
            for i in range(4):
                for j in range(4):
                    self.matrix[i][j]=(listaH[0].matrix[i][j]*wagi[0]*wagi[0]+listaH[1].matrix[i][j]*wagi[0]*wagi[1]+listaH[2].matrix[i][j]*wagi[0]*wagi[2]
                        +listaH[3].matrix[i][j]*wagi[1]*wagi[0]+listaH[4].matrix[i][j]*wagi[1]*wagi[1]+listaH[5].matrix[i][j]*wagi[1]*wagi[2]
                        +listaH[6].matrix[i][j]*wagi[2]*wagi[0]+listaH[7].matrix[i][j]*wagi[2]*wagi[1]+listaH[8].matrix[i][j]*wagi[2]*wagi[2])

        elif ilePktC == 4:
            for i in range(4):
                for j in range(4):
                    self.matrix[i][j]=( listaH[0].matrix[i][j]*wagi[0]*wagi[0]+listaH[1].matrix[i][j]*wagi[0]*wagi[1]+listaH[2].matrix[i][j]*wagi[0]*wagi[2]+listaH[3].matrix[i][j]*wagi[0]*wagi[3]
                        + listaH[4].matrix[i][j]*wagi[1]*wagi[0]+listaH[5].matrix[i][j]*wagi[1]*wagi[1]+listaH[6].matrix[i][j]*wagi[1]*wagi[2]+listaH[7].matrix[i][j]*wagi[1]*wagi[3]
                        + listaH[8].matrix[i][j]*wagi[2]*wagi[0]+listaH[9].matrix[i][j]*wagi[2]*wagi[1]+listaH[10].matrix[i][j]*wagi[2]*wagi[2]+listaH[11].matrix[i][j]*wagi[2]*wagi[3]
                        + listaH[12].matrix[i][j] * wagi[3] * wagi[0] + listaH[13].matrix[i][j] * wagi[3] * wagi[1] + listaH[14].matrix[i][j] * wagi[3] * wagi[2] +listaH[15].matrix[i][j] * wagi[3] * wagi[3])

        #return self.matrix

def partialH(elemXY, nrPktC, kt,det,ilePktC):           #liczy macierz H dla konkretnego punktu całkowania
        tempMatrixA = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        tempMatrixB = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        tempMatrixC = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

        for i in range(4):
            for j in range(4):
                tempMatrixA[i][j]=(elemXY.arrX[nrPktC - 1][i] * elemXY.arrX[nrPktC - 1][j])
                tempMatrixB[i][j]=(elemXY.arrY[nrPktC - 1][i] * elemXY.arrY[nrPktC - 1][j])

        if ilePktC == 2:
            for i in range(4):
                for j in range(4):
                    tempMatrixC[i][j]=(kt * (tempMatrixA[i][j] + tempMatrixB[i][j]) *det[nrPktC-1])

        if ilePktC == 3 or ilePktC == 4:
            for i in range(4):
                for j in range(4):
                    tempMatrixC[i][j]=-(kt * (tempMatrixA[i][j] + tempMatrixB[i][j]) *det[nrPktC-1])


        return tempMatrixC

def N1(ksi,eta):
    return 0.25*(1-ksi)*(1-eta)
def N2(ksi,eta):
    return 0.25*(1+ksi)*(1-eta)
def N3(ksi,eta):
    return 0.25*(1+ksi)*(1+eta)
def N4(ksi,eta):
    return 0.25*(1-ksi)*(1+eta)

class bok1:
    ilePktC=0
    wspPktCx =[]
    wspPktCy =[]                                                    # n1  n2  n3  n4
    wartoscN=[[],[],[],[]]#pole w tablicy odp pkt calokowania
                                                               #pc1
                                                               #pc2
    def __init__(self,ilePktC):
        self.ilePktC = ilePktC
        if(self.ilePktC == 2):
            self.wspPktCx.append(-0.57735)   #x pc1
            self.wspPktCx.append(0.57735)    #x pc2
            self.wspPktCy.append(-1)                #y pc1
            self.wspPktCy.append(-1)                #y pc2
            for i in range(self.ilePktC):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))

        elif(ilePktC == 3):
            self.wspPktCx.append(-math.sqrt(3 / 5))
            self.wspPktCx.append(0)
            self.wspPktCx.append(math.sqrt(3 / 5))
            self.wspPktCy.append(-1)
            self.wspPktCy.append(-1)
            self.wspPktCy.append(-1)

            for i in range(self.ilePktC):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))
        elif(ilePktC == 4):
            self.wspPktCx.append(-0.861136)
            self.wspPktCx.append(-0.339981)
            self.wspPktCx.append(0.339981)
            self.wspPktCx.append(0.861136)
            self.wspPktCy.append(-1)
            self.wspPktCy.append(-1)
            self.wspPktCy.append(-1)
            self.wspPktCy.append(-1)

            for i in range(self.ilePktC):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))
class bok2:
    ilePktC=0
    wspPktCx =[]
    wspPktCy =[]
    wartoscN=[[],[],[],[]]


    def __init__(self, ilePktC):
        self.ilePktC = ilePktC
        if (self.ilePktC == 2):
            self.wspPktCx.append(1)                  # x pc1
            self.wspPktCx.append(1)                  # x pc2
            self.wspPktCy.append(-1/math.sqrt(3))    # y pc1
            self.wspPktCy.append(1/math.sqrt(3))     # y pc2
            for i in range(self.ilePktC):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))

        elif (ilePktC == 3):
            self.wspPktCx.append(1)
            self.wspPktCx.append(1)
            self.wspPktCx.append(1)
            self.wspPktCy.append(-math.sqrt(3 / 5))
            self.wspPktCy.append(0)
            self.wspPktCy.append(math.sqrt(3 / 5))

            for i in range(5):
                self.wartoscN.append([])
            for i in range(self.ilePktC):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))
        elif (ilePktC == 4):
            self.wspPktCx.append(1)
            self.wspPktCx.append(1)
            self.wspPktCx.append(1)
            self.wspPktCx.append(1)
            self.wspPktCy.append(-0.861136)
            self.wspPktCy.append(-0.339981)
            self.wspPktCy.append(0.339981)
            self.wspPktCy.append(0.861136)

            for i in range(12):
                self.wartoscN.append([])
            for i in range(self.ilePktC):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))
class bok3:
    ilePktC=0
    wspPktCx =[]
    wspPktCy =[]
    wartoscN = [[], [], [], []]

    def __init__(self, ilePktC):
        self.ilePktC = ilePktC
        if (self.ilePktC == 2):
            self.wspPktCx.append(-1 / math.sqrt(3))  # x pc1
            self.wspPktCx.append(1 / math.sqrt(3))  # x pc2
            self.wspPktCy.append(1)  # y pc1
            self.wspPktCy.append(1)  # y pc2
            for i in range(self.ilePktC):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))

        elif (ilePktC == 3):
            self.wspPktCx.append(-math.sqrt(3 / 5))
            self.wspPktCx.append(0)
            self.wspPktCx.append(math.sqrt(3 / 5))
            self.wspPktCy.append(1)
            self.wspPktCy.append(1)
            self.wspPktCy.append(1)

            for i in range(5):
                self.wartoscN.append([])
            for i in range(self.ilePktC):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))

        elif (ilePktC == 4):
            self.wspPktCx.append(-0.861136)
            self.wspPktCx.append(-0.339981)
            self.wspPktCx.append(0.339981)
            self.wspPktCx.append(0.861136)
            self.wspPktCy.append(1)
            self.wspPktCy.append(1)
            self.wspPktCy.append(1)
            self.wspPktCy.append(1)

            for i in range(12):
                self.wartoscN.append([])
            for i in range(self.ilePktC):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))
class bok4:
    ilePktC=0
    wspPktCx =[]
    wspPktCy =[]
    wartoscN = [[], [], [], []]

    def __init__(self, ilePktC):
        self.ilePktC = ilePktC
        if (self.ilePktC == 2):
            self.wspPktCx.append(-1)  # x pc1
            self.wspPktCx.append(-1)  # x pc2
            self.wspPktCy.append(-1 / math.sqrt(3))  # y pc1
            self.wspPktCy.append(1 / math.sqrt(3))  # y pc2
            for i in range(self.ilePktC):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))

        elif (ilePktC == 3):
            self.wspPktCx.append(-1)
            self.wspPktCx.append(-1)
            self.wspPktCx.append(-1)
            self.wspPktCy.append(-math.sqrt(3 / 5))
            self.wspPktCy.append(0)
            self.wspPktCy.append(math.sqrt(3 / 5))

            for i in range(5):
                self.wartoscN.append([])
            for i in range(self.ilePktC):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))

        elif (ilePktC == 4):
            self.wspPktCx.append(-1)
            self.wspPktCx.append(-1)
            self.wspPktCx.append(-1)
            self.wspPktCx.append(-1)
            self.wspPktCy.append(-0.861136)
            self.wspPktCy.append(-0.339981)
            self.wspPktCy.append(0.339981)
            self.wspPktCy.append(0.861136)

            for i in range(12):
                self.wartoscN.append([])
            for i in range(self.ilePktC):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))

def printBokN(bok):
    print('N1   N2  N3  N4')
    print(str(bok.wartoscN[0][0]) +' '+str(bok.wartoscN[0][1])+' '+str(bok.wartoscN[0][2])+' '+str(bok.wartoscN[0][3]) )
    print(str(bok.wartoscN[1][0]) +' '+str(bok.wartoscN[1][1])+' '+str(bok.wartoscN[1][2])+' '+str(bok.wartoscN[1][3]) )


def partialHbc(bok, ilePktC, alfa,wagi,pk1,pk2):            #liczby macierz hbc dla jednego boku alfa
    matrixHbcPt1=[[],[],[],[]]
    matrixHbcPt2=[[],[],[],[]]
    matrixHbcPt3 = [[], [], [], []]
    matrixHbcPt4 = [[], [], [], []]
    matrixHbc=[[],[],[],[]]


    detJ = (math.sqrt(math.pow((pk2.x-pk1.x), 2) + math.pow((pk2.y-pk1.y), 2))/2)
    if ilePktC == 2:
        for i in range(4):
            for j in range(4):
                matrixHbcPt1[i].append(wagi[0]*(bok.wartoscN[0][i] *bok.wartoscN[0][j]))
                matrixHbcPt2[i].append(wagi[1]*(bok.wartoscN[1][i] *bok.wartoscN[1][j]))

        for i in range(4):
            for j in range(4):
                matrixHbc[i].append(detJ*alfa*(matrixHbcPt1[i][j]+matrixHbcPt2[i][j]))

    elif ilePktC == 3:
        for i in range(4):
            for j in range(4):
                matrixHbcPt1[i].append(wagi[0] * alfa * (bok.wartoscN[0][i] * bok.wartoscN[0][j]))
                matrixHbcPt2[i].append(wagi[1] * alfa * (bok.wartoscN[1][i] * bok.wartoscN[1][j]))
                matrixHbcPt3[i].append(wagi[2] * alfa * (bok.wartoscN[2][i] * bok.wartoscN[2][j]))
        for i in range(4):
            for j in range(4):
                matrixHbc[i].append(detJ * (matrixHbcPt1[i][j] + matrixHbcPt2[i][j] + matrixHbcPt3[i][j]))

    elif ilePktC == 4:
        for i in range(4):
            for j in range(4):
                matrixHbcPt1[i].append(wagi[0] * alfa * (bok.wartoscN[0][i] * bok.wartoscN[0][j]))
                matrixHbcPt2[i].append(wagi[1] * alfa * (bok.wartoscN[1][i] * bok.wartoscN[1][j]))
                matrixHbcPt3[i].append(wagi[2] * alfa * (bok.wartoscN[2][i] * bok.wartoscN[2][j]))
                matrixHbcPt4[i].append(wagi[3] * alfa * (bok.wartoscN[3][i] * bok.wartoscN[3][j]))
        for i in range(4):
            for j in range(4):
                matrixHbc[i].append(detJ * (matrixHbcPt1[i][j] + matrixHbcPt2[i][j] + matrixHbcPt3[i][j]+matrixHbcPt4[i][j]))

    return matrixHbc

def margeHbc(m1,m2,m3,m4):              #złacenie macierzy dla kazdego boku do jedenej dla calego elementu
    finalMatrixHbc=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            finalMatrixHbc[i][j]=round(m1[i][j]+m2[i][j]+m3[i][j]+m4[i][j],2)
    return finalMatrixHbc

def printHbc(matrix):
    for i in range(4):
        print(str(matrix[i][0])+ ' '+str(matrix[i][1])+ ' '+str(matrix[i][2])+ ' '+str(matrix[i][3]))
    print()
