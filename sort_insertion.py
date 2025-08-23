# keep left side sorted and insert each number from right side  is their proper position.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    arr = [5, 6, 1, 3]
    insertion_sort(arr)
    print(arr)

    arr = [9, 19, -11, 1, -3]
    insertion_sort(arr)
    print(arr)
