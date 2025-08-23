# In an array of ints, print diff combination of numbers i.e
# Arr: 1 2 3 4
# o/p: 1, 2, 3, 4, 12, 13, 14, 23, 24, 34, 123, 134, ...

def generate_combinations(arr):
    result = []
    n = len(arr)

    def backtrack(start, path):
        # Save current path (combination)
        if path:
            # convert list [1,2,3] → int(123)
            num = int("".join(map(str, path)))
            result.append(num)

        # Try including each element after 'start'
        for i in range(start, n):
            backtrack(i + 1, path + [arr[i]])      # move forward

    backtrack(0, [])
    return result


# Example usage
arr = [1, 2, 3, 4]
print(generate_combinations(arr))
