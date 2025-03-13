
def bubble_sort(input):
    for i in range(len(input)):
        for j in range(i, len(input)):
            if input[i]>input[j]:
                temp = input[i]
                input[i] = input[j]
                input[j] = temp
    return input


input = [1,4,6,9,-1,3,0]
print(input)
print(bubble_sort(input))