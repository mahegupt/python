# Given an array nums and an integer k, return the kth largest element in the array.
# Example: nums = [3,2,1,5,6,4], k = 2 → Output: 5
import heapq

# Using in-built sort


def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]


# Example
array = [3, 2, 3, 1, 2, 14, 51, 15, 16]
k = 3
print(f"K={k}th largest in array - {array} is {findKthLargest(array, k)}")


''' Using heap queue.
Python’s heapq is a min-heap by default.
Maintain a min-heap of size k.
Push numbers, pop smallest when size exceeds k.
Top of heap = k-th largest.'''


def findKthLargest_heap(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]


# Example
array = [3, 2, 3, 1, 2, 14, 51, 15, 16]
print(f"K={k}th largest in array - {array} is {findKthLargest_heap(array, k)}")


def quickselect(nums, k):
    # kth largest is (len(nums) - k)th smallest in zero-based index
    k = len(nums) - k
    left, right = 0, len(nums) - 1
    while True:
        pivot = partition(nums, left, right)
        if pivot == k:
            return nums[pivot]
        elif pivot < k:
            left = pivot + 1
        else:
            right = pivot - 1


def partition(nums, left, right):
    # choose rightmost as pivot
    pivot_val = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] < pivot_val:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i


array = [3, 2, 3, 1, 2, 14, 51, 15, 16]
print(f"K={k}th largest in array - {array} is {quickselect(array, k)}")
