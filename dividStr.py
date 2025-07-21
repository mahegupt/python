from typing import List


class Solution:
    def divideString1(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        output = []
        for i in range(0, n, k):
            chunk = s[i:i+k]
            if len(chunk) < k:
                chunk += fill * (k-len(chunk))
            output.append(chunk)
        return output

    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        if n % k != 0:
            s += fill*(k - n % k)
        return [s[i:i+k] for i in range(0, len(s), k)]


data = input()
s = Solution()
print(s.divideString(data, 3, 'x'))
