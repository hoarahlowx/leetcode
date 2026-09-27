class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ln = len(nums)
        ans = 0
        for i in range(ln):
            for j in range(i + 1, ln):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans