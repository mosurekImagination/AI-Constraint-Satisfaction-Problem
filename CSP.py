from enum import Enum

class CSP:

    class Heurestic(Enum):
        TAKE_FIRST = 1
        MIN_DOMAIN = 2
        MAX_CONSTRAINT = 3


    def __init__(self):
        self.variableList = []
        self.domain = 0
        return

    def initialiseProblem(self, heurestic = Heurestic.TAKE_FIRST):
        return

    def checkConstraints(self, elem):
        return

    def clearElem(self,elem):
        return

    def generateVariableList(self):
        return

    def increaseElem(self, elem):
        return

    def getValueElem(self, elem):
        return


    def solveProblem(self):
        accElem = 0
        while(accElem < len(self.variableList)):
          #  print(self.graph)
            if accElem == -1:
                self.domain += 1
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
            else:
                continue


