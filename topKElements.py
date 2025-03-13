from collections import Counter

def topKFrequent(nums, k):
    freq_map = {}
    freq_map = Counter(nums)
    bucket = [[] for _ in range(len(nums) + 1)]  # Step 2: Create bucket array

    # Step 3: Populate bucket with numbers based on frequency
    for num, freq in freq_map.items():
        bucket[freq].append(num)
        
    print(bucket)
    print(freq_map)
    # Step 4: Extract top k elements
    result = []
    for i in range(len(bucket) - 1, 0, -1):  # Start from highest frequency
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result  # Return first k elements found

    return result

nums = [4,4,4,6,6,2,2,2,2]
k = 2
print(topKFrequent(nums, k)) 

nums = [1,2]
k = 2
print(topKFrequent(nums, k)) 