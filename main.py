from ColorGraph import ColorGraph
from CSP import CSP

graphCSP = ColorGraph(size=4, initDomainSize=6)
graphCSP.solveProblem(CSP.VariableHeurestic.TAKE_FIRST,CSP.SolveHeurestic.BACK_TRACKING)
print("Solved CSP graph BACKTRACKING:")
backtracking = len(graphCSP.results)
print(backtracking)
print(graphCSP.getExecutionTime())

graphCSP = ColorGraph(size=4, initDomainSize=6)
graphCSP.solveProblem(CSP.VariableHeurestic.TAKE_FIRST,CSP.SolveHeurestic.FORWARD_TRACKING)
print("Solved CSP graph FORWARD:")
print(len(graphCSP.results))
forward = len(graphCSP.results)
print(graphCSP.getExecutionTime())
print("backtracking: ", backtracking, " Forward: ", forward)
