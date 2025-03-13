import pdb
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). 
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        pdb.set_trace()
        p = 0
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1):
                    p += 4
                    #Subtract 2 for shared edge to avoid double counting i.e.1 edge from both cell.                    
                    if r>0 and grid[r-1][c] == 1:
                        p -= 2
                    if c>0 and grid[r][c-1] == 1:
                        p -= 2
        return p

if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    sol = Solution()
    print(f"grid is {grid} and parameter is {sol.islandPerimeter(grid)}")