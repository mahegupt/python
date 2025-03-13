# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

def longestPrefix(strs):
    if len(strs)==0:
        return ""
    
     # Start with the first string as the common prefix
    prefix = strs[0]

    # Compare the prefix with next string onward in strs
    for j in range(1, len(strs)):
        while not strs[j].startswith(prefix):
            ##Shorten the prefix by removing chars from end.
            prefix = prefix[:-1]
            if prefix == "":
                return prefix
    return prefix

if __name__=="__main__":
    strs = ["flower","flow","fight"]
    print(f"prefix of {strs} is {longestPrefix(strs)}")

            