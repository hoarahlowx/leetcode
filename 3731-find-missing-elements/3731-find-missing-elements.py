from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 != nums[i]:
                ans.extend([j for j in range(nums[i - 1] + 1, nums[i])])
        return ans
    