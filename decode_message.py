###
###We have a message consisting of digits 0-9 to decode. Letters are encoded to digits by their positions in the alphabet
###
### A -> 1
### B -> 2
### C -> 3
### ...
###Y -> 25
###Z -> 26
### Given a non-empty string of digits, how many ways are there to decode it?
### 
### Input: 
###

def decode_ways(digits: str) -> int:
    def dfs(digits: str, start_index: int):
        if start_index == len(digits):
            return 1

        # can't decode string with leading 0
        if digits[start_index] == "0":
            return 0

        ways = 0 
        # decode one digit
        ways += dfs(digits, start_index + 1)

        # decode two digits
        if 10 <= int(digits[start_index : start_index + 2]) <= 26:
            ways += dfs(digits, start_index + 2)

        return ways

    return dfs(digits, 0)

def decode_ways_memo(digits: str) -> int:
    memo: Dict[int, int] = {}
    def dfs(digits: str, start_index: int):
        if start_index in memo:
            return memo[start_index]
        if start_index == len(digits):
            return 1

        # can't decode string with leading 0
        if digits[start_index] == "0":
            return 0

        ways = 0 
        # decode one digit
        ways += dfs(digits, start_index + 1)

        # decode two digits
        if 10 <= int(digits[start_index : start_index + 2]) <= 26:
            ways += dfs(digits, start_index + 2)
        memo[start_index] = ways
        return ways

    return dfs(digits, 0)

##dp[i] as the number of ways to decode the substring s[0:i] (first i characters of s).
# dp[i] += dp[i-1]  or 
# dp[i] += dp[i-2] 
# dp[i] => mean way to decode string of lenght i. dp[1] -> way to decode string of 1 length.
def decode_ways_iter(digits: str):
    if not digits or digits[0] == '0':
        return 0
    n = len(digits)
    dp = [0] * (n+1)
    dp[0], dp[1] = 1, 1 ##Base case.
    for i in range(2, n+1):
        single_digit = int(digits[i-1])    # Last digit
        double_digit = int(digits[i-2:i])

        if 1<= single_digit <= 9:
            dp[i] += dp[i-1]
        if 10<= double_digit<= 26:
            dp[i] += dp[i-2]
    return dp[n]


if __name__ == "__main__":
    digits = "123211434121435123211434121435123211434121435123211434121435"
    # res = decode_ways(digits)
    res = decode_ways_memo(digits)
    print(res)
    res = decode_ways_iter(digits)
    print(res)