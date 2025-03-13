# Given two integers a and b, return any string s such that:
# s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
# The substring 'aaa' does not occur in s, and
# The substring 'bbb' does not occur in s.
 

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []
        ##3 cases are possible with value of a & b.
        ## 1. When a>b
        ## 2. When b > a
        ## 3. when a == b
        while a > 0 or b > 0:
            if a > b:
                if a >= 2:
                    result.append("aa")
                    a -= 2
                else:
                    result.append("a")
                    a -= 1
                if b > 0:
                    result.append("b")
                    b -= 1
            elif b > a:
                if b >= 2:
                    result.append("bb")
                    b -= 2
                else:
                    result.append("b")
                    b -= 1
                if a > 0:
                    result.append("a")
                    a -= 1
            else:
                if a > 0:
                    result.append("a")
                    a -= 1
                if b > 0:
                    result.append("b")
                    b -= 1

        return "".join(result)
    
if __name__ == "__main__":
    s = Solution()
    print(s.strWithout3a3b(2,2))
    print(s.strWithout3a3b(2,5))
    print(s.strWithout3a3b(5,2))
