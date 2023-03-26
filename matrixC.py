def N1(ksi,eta):
    return 0.25*(1-ksi)*(1-eta)

def N2(ksi,eta):
    return 0.25*(1+ksi)*(1-eta)

def N3(ksi,eta):
    return 0.25*(1+ksi)*(1+eta)

def N4(ksi,eta):
    return 0.25*(1-ksi)*(1+eta)

class macierzC:
    # matrix=[[],[],[],[]]   #wartosci juz macierzy
    #ilePktC=0
    wspPktCx =[]    #beda 4 po kolei z indeksami
    wspPktCy =[]    #beda 4 po kolei z indeksami
    wartoscN=[[],[],[],[]]                     # n1  n2  n3  n4
                                            #pc1
                                            #pc2
                                            #pc3
                                            #pc4

    def __init__(self,ilePktC,pktCalkowania):
        self.ilePktC = ilePktC
        self.matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] #macierz C dla jednego punktu

        if(self.ilePktC == 2):
            self.wspPktCx.append(pktCalkowania[0])    #x pc1
            self.wspPktCx.append(pktCalkowania[1])    #x pc2
            self.wspPktCx.append(pktCalkowania[0])    #x pc3
            self.wspPktCx.append(pktCalkowania[1])    #x pc4
            self.wspPktCy.append(pktCalkowania[0])                #y pc1
            self.wspPktCy.append(pktCalkowania[0])                #y pc2
            self.wspPktCy.append(pktCalkowania[1])                #y pc3
            self.wspPktCy.append(pktCalkowania[1])                #y pc4

            for i in range(4):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))

        if (self.ilePktC == 3):
            for i in range(3):
                self.wspPktCx.append(pktCalkowania[0])  # x pc1 4 7
                self.wspPktCx.append(pktCalkowania[1])  # x pc2 5 8
                self.wspPktCx.append(pktCalkowania[2])  # x pc3 6 9

            self.wspPktCy.append(pktCalkowania[0])  # y pc1
            self.wspPktCy.append(pktCalkowania[0])  # y pc2
            self.wspPktCy.append(pktCalkowania[0])  # y pc3
            self.wspPktCy.append(pktCalkowania[1])  # y pc4
            self.wspPktCy.append(pktCalkowania[1])  # y pc5
            self.wspPktCy.append(pktCalkowania[1])  # y pc6
            self.wspPktCy.append(pktCalkowania[2])  # y pc7
            self.wspPktCy.append(pktCalkowania[2])  # y pc8
            self.wspPktCy.append(pktCalkowania[2])  # y pc9

            for i in range(5):
                self.wartoscN.append([])
            for i in range(9):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))

        if(self.ilePktC == 4):
            for i in range(4):
                self.wspPktCx.append(pktCalkowania[0])  # x pc1  4 8
                self.wspPktCx.append(pktCalkowania[1])  # x pc2  5
                self.wspPktCx.append(pktCalkowania[2])  # x pc3  6
                self.wspPktCx.append(pktCalkowania[3])  # x pc3  7

            for i in range(4):
                self.wspPktCy.append(pktCalkowania[0])    #x pc1
            for i in range(4):
                self.wspPktCy.append(pktCalkowania[1])    #x pc1
            for i in range(4):
                self.wspPktCy.append(pktCalkowania[2])  # x pc1
            for i in range(4):
                self.wspPktCy.append(pktCalkowania[3])  # x pc1

            for i in range(12):
                self.wartoscN.append([])
            for i in range(16):
                self.wartoscN[i].append(N1(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N2(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N3(self.wspPktCx[i], self.wspPktCy[i]))
                self.wartoscN[i].append(N4(self.wspPktCx[i], self.wspPktCy[i]))

            #self.matrix = partialC()

        # if (self.ilePktC == 3):
        # if (self.ilePktC == 4):

    def margeC(self,listaH,wagi,ilePktC):          #liczy macierz C finalną sumując i mnożąc przez wagi wszyskie macierze dla poszczególnych punktów całkowania
        if ilePktC == 2:
            for i in range(4):
                for j in range(4):
                    self.matrix[i][j]=(listaH[0].matrix[i][j]*wagi[0]*wagi[0]+listaH[1].matrix[i][j]*wagi[1]*wagi[0]+listaH[2].matrix[i][j]*wagi[0]*wagi[1]
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

    def printArr(self, nrEl):                                                                 #wypisuje końcową macierz H
        #print(f"Macierz dla elementu nr: {nrEl}:")
        for i in range(4):
            print(str(round(self.matrix[i][0],2)) + " " + str(round(self.matrix[i][1],2)) + " " + str(round(self.matrix[i][2],2)) + " " + str(round(self.matrix[i][3],2)))
        print('')

def partialC(N,gestosc,ciepWlasciwe,det, nrPktC,ilePktC): #dla szystkich elementu
    macierzC=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    if ilePktC == 2:
        for i in range(4):          #petla po wektorze transponowanym
            for j in range(4):      #petla po wektorze
                macierzC[i][j] = (N[j]*N[i])*gestosc*ciepWlasciwe*det[nrPktC-1]

    if ilePktC == 3 or ilePktC == 4:
        for i in range(4):          #petla po wektorze transponowanym
            for j in range(4):      #petla po wektorze
                macierzC[i][j] = -(N[j]*N[i])*gestosc*ciepWlasciwe*det[nrPktC-1]

    return macierzC

