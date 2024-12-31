
# Pathfinding Algorithm Visualizer

This program visualizes different pathfinding algorithms that find the shortest path in a grid, considering obstacles (barriers). Users can interact with the grid by setting start and end points, adding barriers, and running different algorithms to find the shortest path.

## Algorithms

The following pathfinding algorithms are implemented:

- **A* Algorithm** (`'A'`)
- **Breadth-First Search (BFS)** (`'B'`)
- **Depth-First Search (DFS)** (`'D'`)
- **Dijkstra's Algorithm** (`'I'`)

## Features

- **Grid Setup**: The grid is a square of `50x50` cells, each representing a node. Users can click on nodes to:
  - Set the **start node** (orange).
  - Set the **end node** (purple).
  - Add **barriers** (black).
  - **Reset** any node by right-clicking on it.

- **Pathfinding Algorithms**: Users can select algorithms to find the shortest path by pressing specific keys:
  - `'A'` - **A\* Algorithm**
  - `'B'` - **Breadth-First Search (BFS)**
  - `'D'` - **Depth-First Search (DFS)**
  - `'I'` - **Dijkstra's Algorithm**
  - `'C'` - **Clear Grid** - Resets the grid, clearing all nodes and barriers.

- **Legend**: The program includes a legend that displays which keys correspond to which algorithms. If no algorithm is selected, the legend is shown on the screen.

## Visuals and Display

The grid is drawn on the window with each cell having a specific color, depending on its state:

- **Orange** for the start node.
- **Purple** for the end node.
- **Black** for barriers.
- **Red** for closed nodes.
- **Green** for open nodes.
- **Blue** for the path.
- **White** for empty spaces.

## Grid Interaction

- **Left-click**: Set the start node (orange) and end node (purple), or add barriers (black).
- **Right-click**: Reset nodes, clearing the start and end points or removing barriers.

## Algorithm Execution

Once the start and end nodes are set, and an algorithm is selected, pressing the corresponding key will trigger the algorithm to find the shortest path between the start and end points. The pathfinding process will be visualized on the grid with different node colors indicating the algorithm's progress.

## Example

Upon running the program, you can set up your grid, select an algorithm using the keys, and the program will visualize the shortest path found between the start and end points, considering barriers on the grid.

