from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(i % 2)
        return sorted(ans)
