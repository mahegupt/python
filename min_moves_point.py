from functools import lru_cache
##reach from point x to point y, only operation allowed is x+1 or x*x for move.

from collections import deque
"""
Use visited and queue data stricture.
"""
def min_moves(x, y):
    queue = deque()
    visited = set()
    queue.append((x, 0))  # (current_value, steps)

    while queue:
        current, steps = queue.popleft()

        if current == y:
            return steps

        if current in visited or current > 2*y:
            continue

        visited.add(current)
        queue.append((current + 1, steps + 1))
        queue.append((current * current, steps + 1))

    return -1  # not reachable

def min_moves1(x, y):
    @lru_cache(maxsize=None)
    def dfs(current):
        if current == y:
            return 0
        if current > y:
            return float('inf')
        return 1 + min(dfs(current + 1), dfs(current * current))
    
    result = dfs(x)
    return result if result != float('inf') else -1


if __name__== "__main__":
    x, y = 1, 100
    print(f"min moves needed from x={x} to y={y} are {min_moves(x,y)}:{min_moves1(x,y)}")
    x, y = 1, 1000
    print(f"min moves needed from x={x} to y={y} are {min_moves(x,y)}:{min_moves1(x,y)}")
    x, y = 1, 100001
    print(f"min moves needed from x={x} to y={y} are {min_moves(x,y)}:{min_moves1(x,y)}")
