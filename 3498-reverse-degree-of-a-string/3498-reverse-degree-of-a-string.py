

class Solution:
    def reverseDegree(self, s: str) -> int:
        letters = 'zyxwvutsrqponmlkjihgfedcba'
        ans = 0
        for i in range(len(s)):
            ans += ((letters.index(s[i]) + 1) * (i + 1))
        return ans