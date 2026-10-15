class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        neg = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            ans *= 10
            ans += x % 10
            x //= 10
            if (neg == 1 and ans > 2 ** 31 - 1) or (neg == -1 and ans > 2 ** 31):
                return 0
        return neg * ans