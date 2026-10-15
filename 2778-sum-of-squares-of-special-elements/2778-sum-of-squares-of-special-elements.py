class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, int(sqrt(len(nums))) + 1):
            if n % i == 0:
                ans += nums[i - 1] ** 2
                if n // i - 1 != i - 1:
                    ans += nums[n // i - 1] ** 2
        return ans