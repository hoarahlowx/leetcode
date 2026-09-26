from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        def backtrack(start: int, cur: int) -> None:
            nonlocal ans
            if start == n:
                ans += cur
                return

            backtrack(start + 1, cur ^ nums[start])
            backtrack(start + 1, cur)
        
        backtrack(0, 0)
        return ans

