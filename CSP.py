from enum import Enum
import numpy as np
import time as tlib
class CSP:

    class VariableHeurestic(Enum):
        TAKE_FIRST = 1
        MIN_DOMAIN = 2
        MAX_CONSTRAINT = 3

    class SolveHeurestic(Enum):
        FORWARD_TRACKING = 9
        BACK_TRACKING = 8


    def __init__(self):
        self.startTime = 0
        self.endTime = 0
        self.variableList = []
        self.domain = 0
        self.domainList = []
        self.results = []
        self.graph=[]
        return

    def checkConstraints(self, elem):
        return

    def clearElem(self,elem):
        return

    def generateVariableList(self, heurestic):
        return

    def increaseElem(self, elem):
        return

    def getValueElem(self, elem):
        return


    def solveProblem(self, variableHeurestic = None, solveHeurestic = None): #
        self.startTime = tlib.time()
        if variableHeurestic is None:
            variableHeurestic = self.VariableHeurestic.TAKE_FIRST
        if solveHeurestic is None:
            solveHeurestic = self.SolveHeurestic.BACK_TRACKING

        self.variableList = self.generateVariableList(variableHeurestic)
        accElem = 0

#####################################################
        if solveHeurestic == self.SolveHeurestic.BACK_TRACKING:
            self.increaseElem(0)
            while(accElem != -1):
                #print(self.graph)
                if accElem == len(self.variableList):
                    print("Znaleziono Rozwiazanie")
                    print(self.graph)
                    self.results.append(self.graph.copy())
                    accElem -= 1
                    self.increaseElem(accElem)
                    continue
                if self.getValueElem(accElem) == self.domain+1:
                    self.clearElem(accElem)
                    accElem-=1
                    self.increaseElem(accElem)
                    continue
                if self.checkConstraints(accElem):
                    accElem+=1
                    if(accElem != len(self.variableList)):
                        self.increaseElem(accElem)
                else:
                    self.increaseElem(accElem)


#####################################################
        if solveHeurestic == self.SolveHeurestic.FORWARD_TRACKING:
            self.initialiseDomains(solveHeurestic)
            self.getNextFromDomain(0)
            self.deleteFromNeighbourDomains(0)
            while(accElem != -1):
                print(self.graph)
                if accElem == len(self.variableList):
                    print("Znaleziono Rozwiazanie")
                    print(self.graph)
                    self.results.append(self.graph.copy())
                    accElem -= 1
                    self.getNextFromDomain(accElem)
                    self.deleteFromNeighbourDomains(accElem)
                    continue
                if (self.checkDomainsNotEmpty()):
                    accElem+=1
                    if(accElem != len(self.variableList)):
                        self.getNextFromDomain(accElem)
                        self.deleteFromNeighbourDomains(accElem)
                else:
                    print("Koniec domeny")
                    print(self.graph)
                    accElem-=1

        self.endTime = tlib.time()

    def increaseDomain(self):
        return

    def initialiseDomains(self, heurestic):
        return

    def checkDomainsNotEmpty(self):
        notEmpty = True
        for i in range(0, len(self.domainList)-1):
            for j in range(0, len(self.domainList)-1):
                if len(self.domainList[i][j]) == 0:
                    return False
        return notEmpty

    def getExecutionTime(self):
        return self.endTime-self.startTime

    def resetNeighbourDomain(self, x,y):
        self.domainList[x][y]

    def resetDomain(self,x,y):
        return

    def getDomain(self,accElem):
        elem = self.variableList[accElem]
        return self.domainList[elem[0]][elem[1]]

    def deleteFromNeighbourDomains(self, elem):
        return

    def getNextFromDomain(self, elem):
        return




