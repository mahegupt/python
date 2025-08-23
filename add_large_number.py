def addStrings(num1: str, num2: str) -> str:
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        x = int(num1[i]) if i >= 0 else 0
        y = int(num2[j]) if j >= 0 else 0
        total = x + y + carry
        carry = total // 10
        result.append(str(total % 10))
        i, j = i - 1, j - 1

    return ''.join(result[::-1])


# Example
print(addStrings("987654321987654321987654321", "123456789123456789123456789"))
print(987654321987654321987654321 + 123456789123456789123456789)
