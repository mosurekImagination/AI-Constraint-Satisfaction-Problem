from ColorGraph import ColorGraph
from CSP import CSP

graphCSP = ColorGraph(size=2, initDomainSize=5)
# graphCSP.solveProblem(CSP.VariableHeurestic.TAKE_FIRST,CSP.SolveHeurestic.BACK_TRACKING)
# print("Solved CSP graph:")
# print(len(graphCSP.results))

graphCSP.solveProblem(CSP.VariableHeurestic.TAKE_FIRST,CSP.SolveHeurestic.FORWARD_TRACKING)
print("Solved CSP graph:")
print(len(graphCSP.results))

print(graphCSP.getExecutionTime())
