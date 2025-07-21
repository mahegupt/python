"""
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:
colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).
Return the number of alternating groups.

Input: colors = [0,1,0,1,0], k = 3
Output: 3
Explanation:[0,1,,0], [1,0,1],[0,1,0]

Input: colors = [0,1,0,0,1,0,1], k = 6
Output: 2
Explanation:[0,1,0,1,0,1], [1,0,1,0,1,0]
"""

class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        n = len(colors)
        count = 0

        for i in range(n):  # Start from every index
            is_alternating = True
            for j in range(1, k):  # Check k-length sequence
                prev_index = (i + j - 1) % n
                curr_index = (i + j) % n
                if colors[prev_index] == colors[curr_index]:  # If adjacent elements are same, break
                    is_alternating = False
                    break
            
            if is_alternating:
                count += 1  # Found a valid alternating group
        
        return count

class OptSolution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        n = len(colors)
        count = 0
        alt_count = 1
        for i in range(1, n+k-1):
            curr_index = i%n
            
            if (colors[curr_index] != colors[curr_index-1]):
                alt_count += 1
            else:
                alt_count = 1
            
            if (alt_count>=k):
                count+=1

            if (i>n+k-1):
                break

        return count
    
if __name__ == "__main__":
    s = Solution()
    os = OptSolution()
    colors = [0,1,0,0,1,0,1]
    k = 6
    print(f"colors={colors}, k={k}, and #alternating groups {s.numberOfAlternatingGroups(colors, k)}")
    print(f"colors={colors}, k={k}, and #alternating groups {os.numberOfAlternatingGroups(colors, k)}")
    colors = [0,1,0,1]
    k = 3
    print(f"colors={colors}, k={k}, and #alternating groups {s.numberOfAlternatingGroups(colors, k)}")
    print(f"colors={colors}, k={k}, and #alternating groups {os.numberOfAlternatingGroups(colors, k)}")