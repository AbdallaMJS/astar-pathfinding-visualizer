# A* Pathfinding Algorithm & Visualizer

A clean, Python-based implementation of the A* (A-Star) pathfinding algorithm, featuring a real-time console visualization. This project demonstrates core computer science competencies, specifically in data structures (priority queues/heaps) and algorithmic problem-solving.

## 🌟 Key Features

- **Optimal Pathfinding:** Implements the A* algorithm to find the shortest path between a start and end point on a 2D grid.
- **Heuristic Search:** Uses the Euclidean distance heuristic to prioritize nodes that bring the path closer to the goal, making it significantly more efficient than standard Dijkstra's algorithm.
- **Real-Time Console Visualization:** Visually animates the search process directly in the terminal, showing the algorithm exploring nodes ('O') and finally tracing the optimal path ('*') around obstacles ('1').
- **Clean Architecture:** Object-oriented design separating the `Node` structure from the search logic, ensuring readable and maintainable code.

## 🛠️ Technologies Used

- **Language:** Python
- **Data Structures:** Lists, Tuples, `heapq` (Priority Queue for efficient node selection)

## 💡 How It Works

The A* algorithm works by maintaining two lists: an *open list* (nodes to be evaluated) and a *closed list* (nodes already evaluated). 
For each node, it calculates three values:
- `g`: The exact cost to reach this node from the starting point.
- `h`: The heuristic estimated cost to reach the destination from this node.
- `f`: The total cost (`g + h`).

At each step, the algorithm explores the node in the open list with the lowest `f` value, heavily optimizing the search direction.

## 🚀 Setup and Execution

No external libraries (like NumPy or Pygame) are required. This project relies purely on Python's standard library.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AbdallaMJS/astar-pathfinding-visualizer.git
   cd astar-pathfinding-visualizer
   ```

2. **Run the script:**
   ```bash
   python astar.py
   ```
   Watch the terminal as the algorithm navigates the maze!

## 🧠 Educational Value & MBZUAI Relevance

This project is highly relevant to undergraduate AI studies. Pathfinding algorithms form the basis of many AI applications, from robotics and autonomous navigation to game AI. By implementing A* from scratch rather than using a library, it demonstrates a deep understanding of graph traversal, heuristic functions, and the practical application of data structures like priority queues to optimize algorithm time-complexity.

---
*Developed by Abdalla M.J.S. Alblooshi to showcase foundational algorithmic skills and computational thinking.*
