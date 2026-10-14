class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = '-'
        if (dividend <= 0 and divisor < 0) or (dividend >= 0 and divisor > 0):
            neg = ''
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        for i in range(31, -1, -1):
            if (divisor << i) <= dividend:
                dividend -= divisor << i
                ans += 1 << i
        ans = int(neg + str(ans))
        if -2**31 > ans:
            return -2**31
        if 2**31 - 1 < ans:
            return 2**31 - 1
        return ans
