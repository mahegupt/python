def bubble_sort(nums):
    n = len(nums)
    swapped = False
    for i in range(n):
        for j in range(n-i-1):
            if (nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    arr = [5, 6, 1, 3]
    bubble_sort(arr)
    print(arr)

    arr = [9, 19, -11, 1, -3]
    bubble_sort(arr)
    print(arr)
