def ones_in_bin(n):
    ans = 0
    while n > 0:
        if n % 2 == 1:
            ans += 1
        n //= 2
    return ans


class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []
        for i in range(n + 1):
            ans.append(ones_in_bin(i))
        return ans
        