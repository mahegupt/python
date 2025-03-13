from collections import Counter

def get_top_k_most_frequent_numbers(nums, k):
    counts_num = Counter(nums)
    x = sorted(counts_num.items(), key=lambda x: x[1], reverse=True) 
    return [x[i][0] for i in range(k)]

nums = [1,1,1,2,2,3]
k = 2
print(get_top_k_most_frequent_numbers(nums, k))