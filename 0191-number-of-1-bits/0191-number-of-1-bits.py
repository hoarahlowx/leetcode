class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        i = 0
        while i ** 2 <= n + 1:
            ans += (n >> i) & 1
            i += 1
        return ans