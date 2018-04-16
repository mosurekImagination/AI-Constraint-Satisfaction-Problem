from enum import Enum
import numpy as np
import time as tlib


class CSP:
    CHECKED = -1

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
                #print(self.graph)
                if accElem == len(self.variableList):
                    self.results.append(self.graph.copy())
                    print("Znaleziono Rozwiazanie")
                    accElem -= 1
                    self.restoreFromNeighbourDomain(accElem)
                    self.getNextFromDomain(accElem)
                    self.deleteFromNeighbourDomains(accElem)
                    continue
                if (self.checkDomainsNotEmpty() and not self.getValueElem(accElem) == CSP.CHECKED):
                    accElem+=1
                    if(accElem != len(self.variableList)):
                        self.restoreFromNeighbourDomain(accElem)
                        self.getNextFromDomain(accElem)
                        self.deleteFromNeighbourDomains(accElem)
                else:
                    if(self.getValueElem(accElem) == CSP.CHECKED):
                        if (accElem == 0):
                            break;
                        self.restoreFromNeighbourDomain(accElem)
                        self.resetValue(accElem)
                        accElem-=1
                        self.restoreFromNeighbourDomain(accElem)
                        self.getNextFromDomain(accElem)
                        self.deleteFromNeighbourDomains(accElem)
                    elif( not self.isLastInDomain(accElem) ):
                        self.restoreFromNeighbourDomain(accElem)
                        self.getNextFromDomain(accElem)
                        self.deleteFromNeighbourDomains(accElem)
                    else:
                        self.restoreFromNeighbourDomain(accElem-1)
                        self.restoreFromNeighbourDomain(accElem)
                        self.getNextFromDomain(accElem-1, back=True)
                        self.resetValue(accElem)
                        accElem-=1
                        self.deleteFromNeighbourDomains(accElem)

        self.endTime = tlib.time()

    def increaseDomain(self):
        return

    def initialiseDomains(self, heurestic):
        return

    def checkDomainsNotEmpty(self):
        notEmpty = True
        for i in range(0, len(self.domainList)):
            for j in range(0, len(self.domainList)):
                if len(self.domainList[i][j]) == 0:
                    return False
        return notEmpty

    def getExecutionTime(self):
        return self.endTime-self.startTime

    def resetDomain(self,x,y):
        return

    def getDomain(self,accElem):
        elem = self.variableList[accElem]
        return self.domainList[elem[0]][elem[1]]

    def deleteFromNeighbourDomains(self, elem):
        return

    def getNextFromDomain(self, elem):
        return

    def restoreFromNeighbourDomain(self, elem):
        return

    def isLastInDomain(self, accElem):
        pass

    def resetValue(self, accElem):
        pass






