class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')
        for i in nums:
            ans = min(ans, sum([int(i) for i in str(i)]))
        return ans