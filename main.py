from ColorGraph import ColorGraph
from CSP import CSP

graphCSP = ColorGraph(size=4, initDomainSize=5)
graphCSP.initialiseProblem()
graphCSP.solveProblem()
print("Solved CSP graph:")
print(graphCSP.graph)
