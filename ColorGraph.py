from CSP import CSP
import numpy as np


class ColorGraph(CSP):

    def __init__(self, size, initDomainSize = 1, minOdds = 1):
        self.size = size
        self.graph = np.zeros((self.size, self.size), dtype=int)
        self.domain = initDomainSize
        self.minOdds = minOdds
        self.results = []

    def generateVariableList(self, heurestic):
        list=[]
        if heurestic == CSP.VariableHeurestic.TAKE_FIRST:
            for i in range (0,self.size):
                for j in range (0,self.size):
                    list.append((i,j))
        return list

    # def initialiseProblem(self, firstVariableHeurestic = CSP.SolveHeurestic.TAKE_FIRST):
    #     accElem = 0
    #     while(accElem < len(self.variableList)):
    #         print(self.graph)
    #         if accElem == -1:
    #             self.increaseDomain()
    #             accElem = 0
    #             #print("Domain raised to: {}".format(self.domain))
    #             continue
    #         if self.getValueElem(accElem) > self.domain:
    #             self.clearElem(accElem)
    #             accElem-=1
    #             #print("Element cross Domain: ")
    #             continue
    #
    #         self.increaseElem(accElem)
    #         if self.checkConstraints(accElem) :
    #             accElem+=1
    #             continue



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

    def resetDomain(self,x,y,value):
        if (x >= 0 and y >= 0 and x < self.size and y < self.size):
            self.domainList[x][y] =(np.arange(1, self.domain))

    def resetNeighbourDomain(self, x,y):
        self.graph[x][y]=0
        self.resetDomain(x+1,y+1,value)
        self.resetDomain(x+1,y-1)
        self.resetDomain(x,y+1)
        self.resetDomain(x,y-1)
        self.resetDomain(x+1,y)
        self.resetDomain(x-1,y)
        self.resetDomain(x-1,y+1)
        self.resetDomain(x-1,y-1)


    def deleteFromNeighbourDomains(self, elem):
        elem = self.variableList[elem]
        x = elem[0]
        y = elem[1]
        value = self.graph[x][y]

        ## Bezposredni Sasiedzi
        self.deleteBannedValue(x-1, y, (value, value+1, value-1))
        self.deleteBannedValue(x+1, y, (value, value+1, value-1))
        self.deleteBannedValue(x, y-1, (value, value+1, value-1))
        self.deleteBannedValue(x, y+1, (value, value+1, value-1))

        #Skos
        self.deleteBannedValue(x+1, y+1, (value,))
        self.deleteBannedValue(x-1, y+1, (value,))
        self.deleteBannedValue(x+1, y-1, (value,))
        self.deleteBannedValue(x-1, y-1, (value,))


    def deleteBannedValue(self,x,y,value):
        if (x >= 0 and y >= 0 and x < self.size and y < self.size):
            for i in range (0,len(value)):
                #print(x,"y:",y)
                #print(value[i])
                #print(self.domainList[x][y])
                if(x == 1 and y == 1):
                    a = 5
                index = np.where(self.domainList[x][y]==value[i])[0]
                if (len(index) != 0):
                    self.domainList[x][y] = np.delete(self.domainList[x][y],index[0])
                   # print("Po usunieciu", self.domainList[x][y])


    def addDomainValue(self, elem, value):
        x = elem[0]
        y = elem[1]
        self.getDomain(elem).push(value)

    def getNextFromDomain(self, elem):
        value = self.getValueElem(elem)
        domain = self.getDomain(elem)
        if (value == 0 ):
            self.setElemValue(elem, domain[0])
        index = np.nonzero(domain == self.getValueElem(elem))[0][0]
        self.setElemValue(elem, domain[index])

    def setElemValue(self, accElem, value):
        elem = self.variableList[accElem]
        self.graph[elem[0]][elem[1]] = value






