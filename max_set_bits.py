## To return a maximum number that shows the longest contiguous “1” bits in a 32-bit integer when flipping a “0” to “1”. (without considering performance).
##Solution: find the longest contiguous sequence of 1s in a 32-bit integer when we are allowed to flip exactly one 0 to 1, Split the binary reprsentation of number by 0.
##  For each 0, check the number of 1s on the left and right of that 0.
## Comput the max length by considering 1 flip of 0 to 1 between each subset of 1.
def max_set_bits(n):
    bnum = bin(n)[2:] ##Convert the number to binary, get 0 and 1, except first few chars.
    sets_one = bnum.split('0')

    if(len(sets_one) == 1):
        return len(sets_one)
    else:
        #count number of set bits 
        max_len = 0
        for i in range(len(sets_one)-1):
            curr_len = len(sets_one[i]) + 1 + len(sets_one[i+1])
            max_len = max(max_len, curr_len)

    return max_len

n = 0b110111011011  # Binary representation: "11011101111"
print(max_set_bits(n))  # Output: 8