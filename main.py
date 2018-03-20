from ColorGraph import ColorGraph
from CSP import CSP

graphCSP = ColorGraph(3)
graphCSP.initialiseProblem(CSP.Heurestic.TAKE_FIRST)
print(graphCSP.graph)
print(graphCSP.variableList)
