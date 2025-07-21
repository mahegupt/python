def merge_sorted_lists(l1, l2):
    merged_list = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1
    merged_list.extend(l1[i:])
    merged_list.extend(l2[j:])
    return merged_list


if __name__ == "__main__":
    l1 = [1,5,16,19]
    l2 = [3,100]
    mergeList = merge_sorted_lists(l1, l2)
    print(f"merge list of {l1} and {l2} is {mergeList}")
    
    