from ColorGraph import ColorGraph
from CSP import CSP

graphCSP = ColorGraph(size=3, initDomainSize=5)
graphCSP.solveProblem(CSP.VariableHeurestic.TAKE_FIRST,CSP.SolveHeurestic.BACK_TRACKING)
print("Solved CSP graph:")
print(len(graphCSP.results))

print(graphCSP.getExecutionTime())
