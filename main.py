from ColorGraph import ColorGraph
from CSP import CSP

graphCSP = ColorGraph(size=8, initDomainSize=5)
graphCSP.solveProblem(CSP.VariableHeurestic.TAKE_FIRST,CSP.SolveHeurestic.BACK_TRACKING)
print("Solved CSP graph:")
print(graphCSP.graph)

print(graphCSP.getExecutionTime())
