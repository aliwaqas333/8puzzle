# 8puzzle
Python script for solving the classic "8-puzzle" game using A start algorithm.

# Capabilities
- It can print out the least amount of steps required to solve 8puzzle at any given state
- It can print out all the steps required to solve 8puzzle from the initial state
- It can detect whether the given 8puzzle state is possible to be solved

## Input Method
for inputing a state to be executed, you will have to edit the `istate` variable in `puzzlelogics.py` file
Example of input state: 

`istate = [
    [2, 5, 4],
    [6, 1, 3],
    [0, 7, 8]
]`

`0` shows the empty square . while target state will be 

`targetState = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]`


# Running the program
open command pannel in the directory of the project and run `python main.py`

once the command is executed, you will see all the steps required to solve the input state. 


# A star algortihm     `f(n) = h(n) + g(n)`
A* (pronounced "A-star") is a graph traversal and path search algorithm, which is often used in computer science due to its completeness, optimality, and optimal efficiency. One major practical drawback is its {\displaystyle O(b^{d})}O(b^d) space complexity, as it stores all generated nodes in memory. Thus, in practical travel-routing systems, it is generally outperformed by algorithms which can pre-process the graph to attain better performance, as well as memory-bounded approaches; however, A* is still the best solution in many cases.

## How A* solves 8puzzle?
This is explained in detail here [Solving 8-Puzzle using A* Algorithm](https://blog.goodaudience.com/solving-8-puzzle-using-a-algorithm-7b509c331288).

## Heuristic Function
The average solution cost for a randomly generated 8-puzzle instance is about 22 steps.The branching factor is about 3. (When the empty tile is in the middle, four moves are possible; when it is in a corner, two; and when it is along an edge, three.) This means that an exhaustive tree search to depth 22 would look at about 322 ≈ 3.1×1010 states.

## Measuring H(n)
To measure H(n) for a given state, we calculate the distance of each tile from target state and sum them up. 
`the sum of the distances of the tiles from their goal positions. Because tiles
cannot move along diagonals, the distance we will count is the sum of the horizontal
and vertical distances. This is sometimes called the city block distance or Manhattan
distance.`

for a `state = [
    [2, 5, 4],
    [6, 1, 3],
    [0, 7, 8]
]`
H(n) will be 1+1+3+2+2+1+2+1+1 = 14

A* algortihm will explore state with least H(n) + g(n) where g(n) is the actual distance
## Programing Language:
Python

