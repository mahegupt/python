def binary_search(nums, num):
    if not nums:
        return -1
    else:
        start = 0
        end = len(nums)
        while (start <= end):
            mid = (start + end) // 2
            if (nums[mid] == num):
                return mid
            elif (nums[mid] < num):
                start = mid + 1
            else:
                end = mid - 1
    return -1


if __name__ == "__main__":
    nums = [1, 4, 6, 7, 9, 11, 15, 21]
    num = 11
    print(f"{num} is at index {binary_search(nums, num)} in nums list {nums}")
    num = 21
    print(f"{num} is at index {binary_search(nums, num)} in nums list {nums}")
    num = 4
    print(f"{num} is at index {binary_search(nums, num)} in nums list {nums}")

    input = ""
