# Given two positive integers a and b, return the number of common factors of a and b.
# An integer x is a common factor of a and b if x divides both a and b.
# Input: a = 12, b = 6
# Output: 4
# Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.

from typing import Tuple, List

class Solution:
    def gcd(self, a, b):
        while(b>0):
            a, b = b, a%b
        return a

    def commonFactors(self, a: int, b: int) -> Tuple[int, List[int]]:
        gd = self.gcd(a, b)
        count = 0
        result = []
        for i in range(1, gd+1):
            if a%i==0 and b%i==0:
                result.append(i)
                count+=1
        return count, result
        

if __name__ == "__main__":
    a=20
    b=30
    sol = Solution()
    n, factors = sol.commonFactors(a, b)
    print(f'For a={a} and b={b}, there are {n} of common factors are {factors}')