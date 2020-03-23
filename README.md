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


## Programing Language:
Python

