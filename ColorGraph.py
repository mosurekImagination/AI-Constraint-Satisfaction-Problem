from CSP import CSP
import numpy as np


class ColorGraph(CSP):

    def __init__(self, size, initDomainSize = 1, minOdds = 2):
        self.size = size
        self.graph = np.zeros((self.size, self.size), dtype=int)
        self.domain = initDomainSize
        self.minOdds = minOdds

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
        correct = self.checkNotEqual(x-1, y, value) and self.checkNotEqual(x+1, y, value)
        if not correct:
            return False
        correct = self.checkNotEqual(x, y-1, value) and self.checkNotEqual(x, y+1, value)
        if not correct:
            return False
        correct = self.checkMinOdds(x+2, y, value) and self.checkMinOdds(x-2, y, value)
        if not correct:
            return False
        correct = self.checkMinOdds(x, y+2, value) and self.checkMinOdds(x, y-2, value)
        if not correct:
            return False
        correct = self.checkMinOdds(x-1, y-1, value) and self.checkMinOdds(x-1, y+1, value)
        if not correct:
            return False
        correct = self.checkMinOdds(x+1, y-1, value) and self.checkMinOdds(x+1, y+1, value)
        if not correct:
            return False

        return correct

    def initialiseDomains(self, heurestic):
        if heurestic == self.SolveHeurestic.BACK_TRACKING:
            self.domain = 0
        if heurestic == self.SolveHeurestic.FORWARD_TRACKING:
            self.domainList = np.range(self.size)
            for i in range(0, self.size):
                self.domainList[i] = np.range(self.size)
                for j in range (0,self.size):
                    self.domainList[i][j] = (np.arange(1, self.domain))




