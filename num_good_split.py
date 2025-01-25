# You are given a string s.
# A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal to s 
# (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.
# Return the number of good splits you can make in s.
# Input: s = "aacaba"
# Output: 2
# explain - aac, aba is one split, aaca, ba is another split.



class GoodSplitsCounter:
    # def __init__(self, s):
    #     self.s = s

    def numSplits(self, s: str) -> int:
        n =  len(s)
        left_uniq_count = [0] * n
        right_uniq_count = [0] * n
        
        #Count unique character seen from left till end for each index.
        visited = set() 
        for i in range(n):
            visited.add(s[i])
            left_uniq_count[i] = len(visited)
        
        #Count unique character seen from left till end for each index.
        visited.clear()
        for i in range(n-1, -1, -1):
            visited.add(s[i])
            right_uniq_count[i] = len(visited)

         # Count the number of good splits on iterating both count set created above.
        good_split = 0
        for i in range(n-1):
            if (left_uniq_count[i] == right_uniq_count[i+1]):
                good_split += 1

        return good_split


# Example Usage
if __name__ == "__main__":
    counter = GoodSplitsCounter()
    print(f"Number of good splits: {counter.numSplits("abcadaabd")}")
    print(f"Number of good splits: {counter.numSplits("aacaba")}")