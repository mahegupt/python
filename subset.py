# Given an array arr = [1, 2, 3], find all possible subsets (including empty set and full array).
# output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

def subsets(nums):
    result = [[]]
    for num in nums:
        result += [curr + [num] for curr in result]
    return result


print(subsets([1, 2, 3]))


def subsets_rec(nums):
    result = []

    def backtrack(start, path):
        # Add current subset (path) to result
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])       # include nums[i]
            backtrack(i + 1, path)    # move to next element
            path.pop()                # backtrack (remove last element)

    backtrack(0, [])
    return result


print(subsets_rec([1, 2, 3]))
