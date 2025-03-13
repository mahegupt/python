##Below function takes O(n) time and 0(n) space.
string = "Hello, World!"
print(string)
reversed_string = string[::-1]
print(reversed_string)


string = "Hello, World!"
reversed_string = ''.join(reversed(string))
print(reversed_string)


##Below function takes O(n^2) time and 0(n) space.
rstring = ""
for c in string:
    rstring = c + rstring
print(rstring)

n=len(string) -1
rstring = ""
while(n>=0) :
    rstring += string[n]
    n -= 1
print(rstring)


##Below function takes O(n) time and 0(n) space.This also work same as reverse() build-in func.
def my_reversed(s):
    for i in range(len(s) - 1, -1, -1):  # Iterate from last index to first
        yield s[i]  # Yield characters one by one

# Example usage
string = "HelloMaheshGupta"
rev_iter = my_reversed(string)  # This mimics reversed(string)
print(string)
print("".join(rev_iter))  # Output: "olleH"