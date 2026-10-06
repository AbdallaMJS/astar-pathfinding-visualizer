import heapq
import time
import os

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance from start node
        self.h = 0  # Distance from end node (heuristic)
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def print_grid(grid, path=None, current_node=None, start=None, end=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    grid_copy = [row[:] for row in grid]
    
    if path:
        for p in path:
            if p != start and p != end:
                grid_copy[p[0]][p[1]] = '*'
                
    if current_node and current_node != start and current_node != end:
        grid_copy[current_node[0]][current_node[1]] = 'O'
        
    grid_copy[start[0]][start[1]] = 'S'
    grid_copy[end[0]][end[1]] = 'E'
    
    print("\n--- A* Pathfinding Progress ---")
    for row in grid_copy:
        print(" ".join(str(val) if str(val) != '0' else '.' for val in row))
    print("S = Start | E = End | 1 = Wall | * = Path | O = Current")
    print("-------------------------------\n")
    time.sleep(0.1)

def astar(grid, start, end):
    start_node = Node(start, None)
    end_node = Node(end, None)

    open_list = []
    closed_list = []
    
    heapq.heappush(open_list, (start_node.f, start_node))

    while len(open_list) > 0:
        current_node = heapq.heappop(open_list)[1]
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if grid[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(node_position, current_node)
            children.append(new_node)

        # Loop through children
        for child in children:
            if child in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if any(open_node for open_node in open_list if child == open_node[1] and child.g > open_node[1].g):
                continue

            heapq.heappush(open_list, (child.f, child))
            
        print_grid(grid, current_node=current_node.position, start=start, end=end)

    return None

if __name__ == '__main__':
    grid = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 8)
    
    print("Starting A* Pathfinding Search...")
    path = astar(grid, start, end)
    
    if path:
        print_grid(grid, path=path, start=start, end=end)
        print("Path found!", path)
    else:
        print("No path found.")
