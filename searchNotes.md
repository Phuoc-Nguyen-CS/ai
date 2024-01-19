## Search

- Agent: An entity that perceives its environment and acts on that environment. (Ex. Cars in a navigation system)

- State: A configuration of the agent within its environment.
    - Initial State: State in which the search algorithm starts.

- Actions: Choices(actions) that can be made within the current state.
    - Upon receiving given state [s] as input. Action(s) returns the output as a set of actions that can be executed in state [s].

- Transition Model: A description of state results from performing any applicable action within any state. Receiving state [s] and action [a] as input. Result(s, a) returns the a new state resulting from state [s] after performing action [a].

- State Space: The set of all states reachable from the initial state by any sequence of actions. They are visualized as a direct graph with states, can be represented as nodes for the states and actions represented as arrows between the nodes.

- Goal State: Checks to see if the given state is the goal state.

- Path Cost: A numerical cost associated with the given path. (Used to find the best path.)

## Solving Search Problems

- A solution is the sequence of actions that leads from initial state -> goal state. But we would want to try to find the optimal solution in which the solution with the **lowest path cost** is chosen.

### Node

- A Node contains these features.

1. A state.
2. A parent node, what was the previous state looking like.
3. The action that was applied to the state of the parent of the current node.
4. The path cost from the initial state to the current node.

### Frontier

1. If frontier empty,
    - *Stop*. There is no solution to the problem.
2. Remove a node from the frontier. This will be the node we are going to consider.
3. If the node is the goal state,
    - Return the solution and *Stop*.
    Else,
    - Expand the node (find all the new nodes that can be reached from this node)
    - Add the current node to the explorered set.
    
### Depth-First Search (DFS)

- A search algorithm that exhausts one direction before trying another direction. (Uninformed)

- Frontier managed as a stack(LIFO) data structure.

- Pros:
    - At best, it is the fastest if you're lucky.
- Cons:
    - The solution it finds may not be optimal
    - At worst, it will explore every possible path before finding the solution.

> The given code removes the last node in the frontier and returns it.

```
def remove(self):
    if self.empty():
        raise Exception('Empty Frontier')
    else:
        node = self.frontier[-1]
        self.frontier = self.frontier[-1]
        return node
```

### Breadth-First Search (BFS)

- Follows multiple directions at the same time, taking one step in each possible direction before taking the second in the each. Uses a queue data structure (FIFO) (Uninformed)

- Pros:
    - Algorithm is guaranteed to find the optimal solution.
- Cons:
    - Algorithm is almost guaranteed to take longer than the minimal amount of time to run.
    - At worst, algorithm takes the longest possible time to run.

> The given code shows removes the first node in the frontier and returns it

```
def remove(self):
    if self.empty():
        raise exception('Empty Frontier')
    else:
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node
```

### Greedy Best-First Search (GBFS)

- (Informed Search Algorithm) Most problems have available information to be used to help assist reach the goal.

- Uses a **heuristic function** *h(n)* to determine how close the node is to the goal. 

- Efficiency depends on how effiencient (GBFS) algorithm is.

- In the context of the maze example: uses Manhattan distance or the distance from current node -> goal node while ignoring walls.

- Due to heuristic, an uninformed search algorithm will provide a better solution at times but it is much less likely than an informed algorithm.

### A* Search (A*)

- An improvment over GBFS as it not only considers *h(n)* but also the cost accrued until the current location *g(n)*.

- The total cost becomes h(n) + g(n)

- For A* to be optimal, the heuristics should be:
    1. Admissible (never overestimating the true cost)
    2. Consistent (consistent when the cost of the new node transitioning from previous node is greater or equal to the estimated path cost from the previous node). h(n) ≤ h(n’) + c where c is the constant.

## Adversarial Search

- The search algorithm used when facing an opponent trying to achieve the opposite goal.

### Minimax

- Winning Condition as (-1) for one side and (+1) for other.

Representing a Tic-Tac-Toe AI:

* S~0: Initial State. (Our case, a 3x3 board)
* Player(s): a function that, given state s, return which player's turn it is. (X or O)
* Action (s): a function that, given state s, returns all the legal moves within the state.
* Result(s, a): a function that, given state s and action a. Returns a new state with the action taken place.
* Terminal(s): a function that, given state s, checks whether this is the last step within the game. Win/Tie/Loss. True if game-over else False.
* Utility(s): a function that, given state s, returns utility value of the state -1, 0, 1.

- Recursively, the algorithm simulates all possible games that take place from the current state until terminal state where each is valued at -1, 0, 

- Given a state s:
    - Max player picks the action *a* in *Action(s)* that produces the highest value for min-value(Result(s,a))
    - Min player picks the action *a* in *Action(s)* that produces the lowest value of max-value(Result(s,a))

### Alpha-Beta Pruning

- To optimize Minimax, prune the branches in which the value is already worse for the player.
