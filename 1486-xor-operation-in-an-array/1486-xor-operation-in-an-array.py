class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start + 0
        t = start + 2
        for i in range(n - 1):
            ans ^= t
            t += 2
            
        return ans