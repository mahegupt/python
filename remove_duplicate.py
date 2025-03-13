def remove_duplicates(input):
    output = set()
    for i in input:
        output.add(i)
    return list(output)

def remove_duplicates_without_set(input):
    hash = {}
    output = []
    for i in input:
        hash[i] += hash.get(i, 0)
    for key in hash.keys:
        output += [key]
    return output

input = [1,2,3,4,56,1,2]
print(input)
print(remove_duplicates(input))
print(remove_duplicates_without_set(input))