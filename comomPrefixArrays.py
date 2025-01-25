# You are given two 0-indexed integer permutations A and B of length n.
# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.
# Return the prefix common array of A and B.
# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.


# Example 1:
# Input: A = [1,3,2,4], B = [3,1,2,4]
# Output: [0,2,3,4]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
# At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
# Example 2:

# Input: A = [2,3,1], B = [3,1,2]
# Output: [0,1,3]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: only 3 is common in A and B, so C[1] = 1.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.


def findThePrefixCommonArray(A, B):
            n = len(A)
            C = [0] * n  # Initialize the prefix common array
            seen_A, seen_B = set(), set()  # Sets to track elements seen so far
            common = 0  # Count of common elements so far

            for i in range(n):
                # Add current elements to their respective sets
                seen_A.add(A[i])
                seen_B.add(B[i])

                if A[i] in seen_B:  # If A[i] is already in B's seen set, it's a common element
                    common += 1
                
                if B[i] in seen_A:  # If B[i] is already in A's seen set, it's a common element
                    common += 1

                if A[i] == B[i]:  # Avoid double counting when A[i] == B[i]
                    common -= 1

                # Store the current count of common elements
                C[i] = common
            print("A=", A, " B=", B, "\nPrefix Common elements count", C)
            return C

findThePrefixCommonArray([1,3,2,4], [3,1,2,4])
findThePrefixCommonArray([2,3,1], [3,1,2])
findThePrefixCommonArray([1,3,4,5], [5,3,4,1])