def counting_sort(arr):
    if not arr:
        return arr

    # Step 1: Find min and max
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    # Step 2: Frequency array
    count = [0] * range_val
    for num in arr:
        count[num - min_val] += 1

    # Step 3: Reconstruct sorted array
    sorted_arr = []
    for i in range(range_val):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr


if __name__ == "__main__":
    arr = [5, 6, 1, 3]
    print(counting_sort(arr))

    arr = [9, 19, -11, 1, -3]
    print(counting_sort(arr))
    print(counting_sort([4, 2, 2, 8, 3, 3, 1]))
