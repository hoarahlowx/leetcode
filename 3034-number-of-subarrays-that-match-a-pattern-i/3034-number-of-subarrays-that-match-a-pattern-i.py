class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        k = len(pattern)
        ans = 0
        for i in range(len(nums) - k):
            f = True
            for n in range(k):
                part = nums[i:i + k + 1]
                if (pattern[n] == 0 and part[n] != part[n + 1]) or (pattern[n] == 1 and part[n] >= part[n + 1]) or (pattern[n] == -1 and part[n] <= part[n + 1]):
                    f = False
                    break
            if f:
                ans += 1
        return ans