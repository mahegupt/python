#Number of Unique Paths to Go from Top Left to Bottom Right
# paths(i,j)=paths(i+1,j)+paths(i,j+1)
# Below code will execute in 2^(m*n)
def unique_paths(m:int, n:int):
    def dfs(i:int, j:int):
        ## If out of bounds, return 0
        if i>=m or j>= n:
            return 0
        # If we reached the destination, return 1
        if i==m-1 and j==n-1:
            return 1
         # Move right and down
        return dfs(i+1, j) + dfs(i, j+1)
    return dfs(0, 0)

def unique_paths(m:int, n:int):
    memo = {}
    def dfs(i:int, j:int):
        ## If out of bounds, return 0
        if i>=m or j>= n:
            return 0
        # If we reached the destination, return 1
        if i==m-1 and j==n-1:
            return 1
        if (i, j) in memo:
            return memo[(i,j)]
         # Move right and down
        memo[(i,j)] =  dfs(i+1, j) + dfs(i, j+1)
        return memo[(i,j)]
    
    return dfs(0, 0)


## Define dp[i][j] as the number of unique paths to reach (i, j).
## Base case: The first row and first column have only one way (either all right or all down).
## Transition:
## dp[i][j] = dp[i-1][j] + dp[i][j-1]
## This means: Ways to reach (i,j) come from above (i-1,j) and left (i,j-1).
# O(m*n)
def uniquePaths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]  # Fill first row & column with 1

    for i in range(1, m):  
        for j in range(1, n):  
            dp[i][j] = dp[i-1][j] + dp[i][j-1]  # Sum from top and left
    
    return dp[m-1][n-1]  # Bottom-right cell
