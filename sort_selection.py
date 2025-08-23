# Repeatedly select the first element from unsorted array, find the smallest (or largest) element from the unsorted
# part of the array and swaps it with the with the selected element.
# Or find the minimum/maximum element in unsorted array and move it to correct position.
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Assume the current position holds
        # the minimum element
        min_idx = i

        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:

                # Update min_idx if a smaller element is found
                min_idx = j

        # Move minimum element to its
        # correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":
    arr = [5, 6, 1, 3]
    selection_sort(arr)
    print(arr)

    arr = [9, 19, -11, 1, -3]
    selection_sort(arr)
    print(arr)
