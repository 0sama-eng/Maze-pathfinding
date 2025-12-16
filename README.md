# Maze Pathfinding

##  Problem Description
Maze pathfinding involves navigating a grid from a **start position** to a **goal position**.  
The maze contains **walls (blocked cells)** and **free cells**.  
The objective is to find a valid path and compare how different search algorithms behave.

---

## Why This Problem?
- The maze has a well-defined **state space**
- You can encode the maze as a **graph**
- The **goal state** is explicit
- Algorithms behave differently (**BFS vs DFS vs A*** etc.)
- Perfect for applying:
  - Uninformed search
  - Informed search
  - Heuristic design
  - Performance comparison

---

## Implementation Approach
- **State Representation:** Each state is represented as a pair `(x, y)`
- **Successor Function:** From each state, generate valid moves `UP`, `DOWN`, `LEFT`, `RIGHT` if no wall prevents the move
- **Cost Function:** Each move has a uniform cost of `1`

###  Heuristic Functions (For A*)
- **Manhattan Distance:** Sum of the distances each tile is from its goal position
- **Euclidean Distance:** Straight-line distance from current position to goal

---

##  Algorithms to Implement
- **BFS (Breadth-First Search):** Guarantees shortest path but may use significant memory
- **DFS (Depth-First Search):** Memory efficient but may not find optimal solution
- **A\* with Manhattan Distance:** Should significantly outperform uninformed search

---

##  BFS in the Maze
### How BFS Works
- Explores the maze **level by level**
- Checks all neighbors of a cell before moving deeper
- Uses a **queue (FIFO)** → first inserted is first expanded
- Expands outward like a **ripple of water**

### Maze Behavior
- BFS spreads evenly from the start node
- Always finds the **shortest path** (minimum steps)
- Requires significant memory to store all frontier nodes

---

##  Deliverables
-  Implementation of all three algorithms
-  Maze visualization + solution path
-  Maze loader or maze generator
-  Performance comparison table
-  Heuristic comparison (A*)
-  Full analysis document
