import copy
# For 8 Puzzle Game - Configuration
# there must be even number of inversions in the starting array for the game to be solvable
istate = [
    [2, 5, 4],
    [6, 1, 3],
    [0, 7, 8]
]
eightStartState = [
    istate,
    [9999, 0], []]
targetState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
fringe = []
closed = []
# 8 Puzzle


def checkSolvable():
    invCount = -1
    for i in range(3):
        for j in range(3):
            if eightStartState[0][j][i] > 0 and eightStartState[0][j][i] > eightStartState[0][i][j]:
                invCount = invCount + 1
    print(invCount)
    return invCount % 2 == 0


def getIndexOf(state, num):  # to get index of a number in the state
    for x in range(len(state)):
        for y in range(len(state)):
            if state[x][y] == num:
                return [x, y]
    return False

# Move functions
def moveLeft(s):
    state = copy.deepcopy(s)
    [x, y] = getIndexOf(state, 0)
    if y < 1: return False
    prevNum = state[x][y-1]
    state[x][y-1] = 0
    state[x][y] = prevNum
    return state


def moveRight(s):
    state = copy.deepcopy(s)
    [x, y] = getIndexOf(state, 0)
    if y > 1: return False
    prevNum = state[x][y + 1]
    state[x][y + 1] = 0
    state[x][y] = prevNum
    return state


def moveUp(s):
    state = copy.deepcopy(s)
    [x, y] = getIndexOf(state, 0)
    if x < 1: return False
    prevNum = state[x-1][y]
    state[x-1][y] = 0
    state[x][y] = prevNum
    return state


def moveDown(s):
    state = copy.deepcopy(s)
    [x, y] = getIndexOf(state, 0)
    if x > 1: return False
    prevNum = state[x+1][y]
    state[x+1][y] = 0
    state[x][y] = prevNum
    return state


def move(state, action):
    if action == 'Left':
        moveLeft(state)
    if action == 'right':
        moveRight(state)
    if action == 'up':
        moveUp(state)
    if action == 'down':
        moveDown(state)
    return False
# move functions end


def calcH(s):
    # h(n)
    state = copy.deepcopy(s)
    h = 0
    for x in range(len(state)):
        for y in range(len(state)):
            default = getIndexOf(state, state[x][y])
            target = getIndexOf(targetState, state[x][y])
            h += abs(default[0] - target[0]) + abs(default[1] - target[1])
    return h


def calcActual(state):
    return state[1][1] + 1

def getNextPossibleStates(state):
    s = copy.deepcopy(state)
    [x, y] = getIndexOf(s[0], 0)
    possibleStates = []
    cost = calcActual(s)
    leftState = moveLeft(list(s[0]))
    rightState = moveRight(list(s[0]))
    upState = moveUp(list(s[0]))
    downState = moveDown(list(s[0]))
    if leftState:
        possibleStates.append([leftState, [calcH(leftState), cost], state])
    if rightState:
        possibleStates.append([rightState, [calcH(rightState), cost], state])
    if upState:
        possibleStates.append([upState, [calcH(upState), cost], state])
    if downState:
        possibleStates.append([downState, [calcH(downState), cost], state])
    return possibleStates


def getLeastState():  # lets get the state with least Heuristic
    if len(fringe) == 0: return [] # return empty list if fringe is empty
    least = fringe[0]
    initialCost = least[1][0] + least[1][1]
    for state in fringe:
        currentCost = state[1][0] + state[1][1]
        if currentCost < initialCost:
            least = state
    return least


def addInFringe(child):  # You can only add if it is not in closed already
    if child[0] not in closed:
        fringe.append(child)


def removeFromFringe(node):
    fringe.remove(node)


def addInClosed(node):
    closed.append(node[0])


def prettyPrint(grid):
    for state in grid:
        print('__________')
        for row in state:
            print(row)
        print('__________')


def getShortestPath(finalState):
    finalState = copy.deepcopy(finalState)
    path = [finalState[0]]
    parent = copy.deepcopy(finalState[2])
    while parent:
        path.append(parent[0])
        parent = parent[2]

    for step in reversed(path):
        prettyPrint([step])

    print("Solved in steps: ", len(path))