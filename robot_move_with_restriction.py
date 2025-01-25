from collections import deque

# Given a rebote on surface, write program to move the robote to target location
# The robot cannot take a direct path to the target. Instead, it must find a valid path while avoiding the restricted cells.

# Problem Setup
# The surface is represented as a 2D grid (matrix).
# Obstacles are marked as 1 (or any non-zero value), while free spaces are 0.
# The robot starts at a position (start_x, start_y) and needs to reach (target_x, target_y).
# Movement is allowed in 4 possible directions: up, down, left, right.
# The robot must navigate around obstacles to find the shortest path to the target.

# Approach
# Use BFS to explore all possible paths from the starting point.
# Maintain a queue of positions to visit. Each entry in the queue includes:
# The current position (x, y)
# The number of steps taken so far


def shortest_path_with_obstacles(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    start_x, start_y = start
    target_x, target_y = target

    # Directions for movement: up, down, left, right
    directions = [(-1, 0, "up"), (1, 0, "down"), (0, -1, "left"), (0, 1, "right")]

    # Initialize visited matrix[m*n], by default, it will be false.
    visited = [[False] * cols for _ in range(rows)]
    visited[start_x][start_y] = True

    # BFS queue: (x, y, steps, path)
    queue = deque([(start_x, start_y, 0, [])])

    while queue:
        x, y, steps, path = queue.popleft()

        # Check if we've reached the target
        if (x, y) == (target_x, target_y):
            return steps, path

        # Explore all possible directions
        for dx, dy, move in directions:
            nx, ny = x + dx, y + dy

            # Check if the next position is valid i.e. with limit of matrix.
            # Check if it is not visited to avoid loop.
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1, path + [move]))

    # If the target is unreachable, return -1
    return -1, []

# Example Usage
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]
start = (0, 0)
target = (3, 3)

steps, path = shortest_path_with_obstacles(grid, start, target)
if steps != -1:
    print(f"Shortest path to reach {target} from {start} takes {steps} steps.")
    print("Path:", " -> ".join(path))
else:
    print(f"Target {target} is unreachable from {start}.")
