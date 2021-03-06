from CSP import CSP
import numpy as np


class ColorGraph(CSP):

    def __init__(self, size, initDomainSize = 1, minOdds = 1):
        self.size = size
        self.graph = np.zeros((self.size, self.size), dtype=int)
        self.domain = initDomainSize
        self.minOdds = minOdds
        self.results = []
        self.bannedElems = np.zeros(self.size * self.size, dtype=object)

    def generateVariableList(self, heurestic):
        list=[]
        if heurestic == CSP.VariableHeurestic.TAKE_FIRST:
            for i in range (0,self.size):
                for j in range (0,self.size):
                    list.append((i,j))
        return list

    def increaseDomain(self):
        self.domain+= 1

    def getValueElem(self, accElem):
        elem = self.variableList[accElem]
        return self.graph[elem[0]][elem[1]]

    def clearElem(self, accElem):
        elem = self.variableList[accElem]
        self.graph[elem[0]][elem[1]] = 0

    def increaseElem(self, accElem):
        elem = self.variableList[accElem]
        self.graph[elem[0]][elem[1]] += 1

    def checkConstraints(self, accElem):
        elem = self.variableList[accElem]
        x = elem[0]
        y = elem[1]
        return self.checkNeighbour(x,y,self.graph[x][y])

    def checkNotEqual(self, x, y, value):
        if(x >= 0 and y >= 0 and x < self.size and y < self.size):
            return self.graph[x][y] != value or self.graph[x][y] == 0   # 0 means it is only initialised
        else:
            return True

    def checkMinOdds(self, x, y, value, minOdds=None):
        if minOdds is None:
            minOdds = self.minOdds

        if( x >= 0 and y >= 0 and x < self.size and y < self.size):
            return np.abs(self.graph[x][y]-value) >= minOdds or self.graph[x][y] == 0   # 0 means it is only initialised
        else:
            return True

    def checkNeighbour(self, x, y, value):
        ##sasiedzi gora dol
        correct = self.checkMinOdds(x-1, y, value, 2) and self.checkMinOdds(x+1, y, value, 2)
        if not correct:
            return False
        correct = self.checkMinOdds(x, y-1, value, 2) and self.checkMinOdds(x, y+1, value, 2)
        if not correct:
            return False

        #sasiedzi skos
        correct = self.checkMinOdds(x+1, y+1, value) and self.checkMinOdds(x-1, y-1, value)
        if not correct:
            return False
        correct = self.checkMinOdds(x-1, y+1, value) and self.checkMinOdds(x+1, y-1, value)
        if not correct:
            return False

        return correct

    def initialiseDomains(self, heurestic):
        if heurestic == self.SolveHeurestic.BACK_TRACKING:
            self.domain = 0
        if heurestic == self.SolveHeurestic.FORWARD_TRACKING:
            self.domainList = np.zeros((self.size, self.size), dtype=object)
            for i in range(0, self.size):
                for j in range (0,self.size):
                    self.domainList[i][j] = (np.arange(1, self.domain+1))
            for i in range(0, self.size* self.size):
                    self.bannedElems[i] = np.arange(0, dtype=(int))

    def resetDomain(self,x,y,value):
        if (x >= 0 and y >= 0 and x < self.size and y < self.size):
            self.domainList[x][y] =(np.arange(1, self.domain))


    def deleteFromNeighbourDomains(self, elem):
        Accelem = self.variableList[elem]
        x = Accelem[0]
        y = Accelem[1]
        value = self.graph[x][y]

        ## Bezposredni Sasiedzi
        self.deleteBannedValue(x-1, y, (value, value+1, value-1), elem)
        self.deleteBannedValue(x+1, y, (value, value+1, value-1), elem)
        self.deleteBannedValue(x, y-1, (value, value+1, value-1), elem)
        self.deleteBannedValue(x, y+1, (value, value+1, value-1), elem)

        #Skos
        self.deleteBannedValue(x+1, y+1, (value,), elem)
        self.deleteBannedValue(x-1, y+1, (value,), elem)
        self.deleteBannedValue(x+1, y-1, (value,), elem)
        self.deleteBannedValue(x-1, y-1, (value,), elem)


    def deleteBannedValue(self,x,y,value, elem):
        if(x == y == 0):
            return
        if (x >= 0 and y >= 0 and x < self.size and y < self.size):
            for i in range (0,len(value)):
                index = np.where(self.domainList[x][y]==value[i])[0]
                if (len(index) != 0):
                    self.domainList[x][y] = np.delete(self.domainList[x][y],index[0])
                    self.bannedElems[elem] = np.append(self.bannedElems[elem], (-self.getElemByCords(x,y), value[i]))



    def addDomainValue(self, elem, value):
        x = elem[0]
        y = elem[1]
        self.getDomain(elem).push(value)

    def getNextFromDomain(self, elem, back = False):
        if(back):
            back = self.getValueElem(elem) == self.domain
        if(self.isLastInDomain(elem) or back):
            self.restoreFromNeighbourDomain(elem)
            self.setElemValue(elem, CSP.CHECKED)
            self.deleteFromNeighbourDomains(elem)

        value = self.getValueElem(elem)
        domain = self.getDomain(elem)
        if (value == 0 ):
            self.setElemValue(elem, domain[0])
            return
        index = np.where(domain == value)[0]
        if (len(index) != 0):
            self.setElemValue(elem, domain[index[0]+1])

    def setElemValue(self, accElem, value):
        elem = self.variableList[accElem]
        self.graph[elem[0]][elem[1]] = value

    def restoreFromNeighbourDomain(self, elem):
        x, y = self.variableList[elem]
        value = self.graph[x][y]

        for i in range (0, int(len(self.bannedElems[elem])/2)):
            RestoreElem = -self.bannedElems[elem][0]
            x, y = self.variableList[RestoreElem]
            value = self.bannedElems[elem][1]
            self.bannedElems[elem] = np.delete(self.bannedElems[elem], [0,1])
            self.domainList[x][y] = np.append(self.domainList[x][y],value)
            self.sortDomain(x,y)

    def restoreBannedValue(self, x, y, value, elem):
        if (x >= 0 and y >= 0 and x < self.size and y < self.size):
            for i in range (0,len(value)):
                index = np.where(self.bannedElems[elem] == -self.getElemByCords(x,y))[0]
                if (len(index) != 0):
                    print(self.graph)
                    self.domainList[x][y] = np.append(self.domainList[x][y],self.bannedElems[elem][index+1])
                    self.bannedElems[elem] = np.delete(self.bannedElems[elem],index[0])
                    self.bannedElems[elem] = np.delete(self.bannedElems[elem], index[0])

    def isLastInDomain(self, elem):
        value = self.getValueElem(elem)
        domain = self.getDomain(elem)
        return np.where(domain == value)[0] == len(domain)-1

    def resetValue(self, elem):
        x,y = self.variableList[elem]
        self.graph[x][y] = 0

    def getElemByCords(self, x, y):
        return x*self.size+y

    def sortDomain(self,x,y):
        self.domainList[x][y]=np.sort(self.domainList[x][y])






