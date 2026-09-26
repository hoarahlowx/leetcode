class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in set(nums):
            if nums.count(i) == 2:
                ans.append(i)
        return ans