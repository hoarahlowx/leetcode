class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        s = sum(nums)
        count = 0
        if k > s:
            return s
        while s % k != 0:
            count += 1
            s -= 1
        return count