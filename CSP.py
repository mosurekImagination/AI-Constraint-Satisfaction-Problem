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
        if solveHeurestic == self.SolveHeurestic.BACK_TRACKING:
            while(accElem < len(self.variableList)):
                if accElem == -1:
                    self.increaseDomain()
                    accElem = 0
                    #print("Domain raised to: {}".format(self.domain))
                    continue
                if self.getValueElem(accElem) > self.domain:
                    self.clearElem(accElem)
                    accElem-=1
                    #print("Element cross Domain: ")
                    continue

                self.increaseElem(accElem)
                if self.checkConstraints(accElem) :
                    accElem+=1
                    continue
        if solveHeurestic == self.SolveHeurestic.FORWARD_TRACKING:
            self.initialiseDomains(solveHeurestic)
            while(accElem < len(self.variableList)):

                accElem+=1
        self.endTime = tlib.time()

    def increaseDomain(self):
        return

    def initialiseDomains(self, heurestic):
        return

    def checkDomainsNotEmpty(self):
        notEmpty = True
        for i in range(0, len(self.variableList)):
            if len(self.domainList[i]) == 0:
                return False
        return notEmpty

    def getExecutionTime(self):
        return self.endTime-self.startTime


