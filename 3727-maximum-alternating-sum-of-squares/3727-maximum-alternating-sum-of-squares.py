class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True, key=lambda x: abs(x))
        ans = sum([i ** 2 for i in nums[:(len(nums) // 2 + (len(nums) % 2))]])
        ans -= sum([i ** 2 for i in nums[(len(nums) // 2 + (len(nums) % 2)):]])
        return ans