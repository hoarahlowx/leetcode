from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        ans = 0
        for left in range(0, len(nums) - 1):
            right = left + 1
            while right < len(nums):
                if nums[right] == nums[left]:
                    ans += 1
                right += 1
        return ans
                    