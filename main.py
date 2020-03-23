from puzzlelogics import *

parent = copy.deepcopy(eightStartState)
print('start')
solvable = True
if checkSolvable() is not True:
    print('Impossible to Solve')
    solvable = False

prettyPrint([parent])
count = 0
found = False
print('parent added to closed')
addInClosed(parent)
print('....working')
while not found:
    children = getNextPossibleStates(parent)
    for child in children:
        addInFringe(child)
        if targetState == child[0]:
            print('**************')
            print('__Found__')
            print('**************')
            found = True
            getShortestPath(child)
            break
    current = getLeastState()  # from fringe
    removeFromFringe(current)
    addInClosed(current)
    parent = current

print('===========Program Ends===================')
# print('moves', closed)


print('Closed items =', len(closed))
print('Fringe items =', len(fringe))
# prettyPrint([closed])