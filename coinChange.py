import sys
sys.setrecursionlimit(10**6)  # Increase recursion limit
"""
Given an array coins of distinct integers (representing coin denominations) and an integer amount, return the fewest number of coins needed to make up that amount.
If that amount cannot be made up by any combination of the coins, return - 
coins = [1, 2, 5] amount = 11
req coins = 3, 5+5+1
1. Dynamic Programming (Bottom-Up)
    dp[i] represents the minimum number of coins needed to make up amount i. We need to find dp[amount].
    dp[0] = 0
    dp[i] = min(dp[i], dp[i-coin]+1) for every coin.

2. Break problem in subproblem, use recurssion with basecase. 
3. Same approach as 2nd but use memoization.
Approach	                        Time Complexity	Space Complexity	Notes
1. DP (Bottom-Up)	                    O(n * amount)	O(amount)	    More efficient for large inputs
2. Recursive (No Memoization)	        O(2^amount)	    O(amount)	    Exponential, very slow
3. Recursive + Memoization (Top-Down)	O(n * amount)	O(amount)	    Optimized recursion
"""

def min_coins_exchange(coins, amount):    
    dp = [float('inf')] * (amount+1)
    dp[0] = 0

    for i in range(amount+1): #Process for each amount.
        for coin in coins: #For each coin.
            dp[i] = min(dp[i], dp[i-coin]+1)

    return dp[amount] if dp[amount] != float('inf') else -1


print(min_coins_exchange([1, 2, 5], 112111))

def rCoinChange(coins, amount):
    memo = {}
    def dfs(coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        if amount in memo:
            return memo[amount]
            
        min_coins = float('inf')
        for coin in coins:
            result = dfs(coins, amount-coin)
            if result != float('inf'):
                min_coins = min(result+1, min_coins)
        memo[amount] = min_coins

        return min_coins        
    
    min_xchange = dfs(coins, amount)
    return min_xchange if min_xchange != float('inf') else -1

print(rCoinChange([1, 2, 5], 112111))

