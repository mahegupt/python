#You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. 
# Two servers are said to communicate if they are on the same row or on the same column.
#Return the number of servers that communicate with any other server.
#Input: grid = [[1,0],[1,1]]
#Output: 3

class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid) #Find number of nodes in grid.
        n = len(grid[0]) #Find number of columns in grid
        serversPerRow = [0] * m
        serversPerColumn = [0] * n
        
        #Count the number of servers in each row and column.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    serversPerRow[i] += 1
                    serversPerColumn[j] += 1

        #Count number of connected servers either in row or in column.
        count = 0
        for i  in range(m):
            for j in range(n):
                if (grid[i][j] == 1 and (serversPerColumn[j]>1) or (serversPerRow[i]>1)):
                    count += 1 

        return count
    
if __name__ == "__main__":
    s = Solution()  
    grid = [
        [1,0,1,1],
        [1,1,0,0]
    ]
    print(grid)
    print(s.countServers(grid))