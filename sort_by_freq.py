# Given an array of integers arr[], sort the array according to the frequency of elements,
# i.e. elements that have higher frequency comes first. If the frequencies of two elements
# are the same, then the smaller number comes first.

from collections import Counter


def frequency_sort(arr):
    freq = Counter(arr)
    # Sort based on (-frequency, value)
    return sorted(arr, key=lambda x: (-freq[x], x))


def frequency_sort2(arr):
    # hash map to store the
    # frequency of each element
    mp = {}
    n = len(arr)

    # store the frequency of each element
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

    # Sort based on (-frequency, value)
    return sorted(arr, key=lambda x: (-mp[x], x))


# Example
arr = [4, 5, 6, 5, 4, 3, 9, 9, 9, 9]
sorted_arr = frequency_sort2(arr)
print(sorted_arr)
