# Encode a String i.e
# aaaabbccdd -> a4b2c2d2

from collections import Counter


def encode(input):
    result = ""
    counts = Counter(input)
    for c in counts:
        result += c + str(counts[c])
    return result


input = "aaaabbbccd"
print(f"input = {input} => {encode(input)}")
