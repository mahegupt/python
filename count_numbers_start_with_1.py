"""
Write a program to find total number starting with 1 in a given range
This question was asked in written test of BIT Capital 
"""
def count_starting_with_one(start, end):
    count = 0
    for num in range(start, end + 1):
        if str(num).startswith('1'):
            count += 1
    return count

"""
Count the number between 2 digits, 3 digits, 4 digits number based on consecutive length.
"""
def count_numbers_starting_with_1(start, end):
    count = 0
    for length in range(len(str(start)), len(str(end)) + 1):
        ##Min number of length(n) digits
        lower = max(start, int('1' + '0' * (length - 1)))
        ##Max number of n digits starting with 1.
        upper = min(end, int('1' + '9' * (length - 1)))
        if lower <= upper:
            count += (upper - lower + 1)
    return count


if __name__=="__main__":
    s, e = 1, 500
    print(f"Numbers start with 1 between {s} and {e} are {count_starting_with_one(s, e)}")
    s, e = 10000, 50000
    print(f"Numbers start with 1 between {s} and {e} are {count_starting_with_one(s, e)}")
    s, e = 1, 999999999
    print(f"Numbers start with 1 between {s} and {e} are {count_numbers_starting_with_1(s, e)}")