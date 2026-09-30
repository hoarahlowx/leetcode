class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = []
        for i in nums:
            t = 0
            for j in nums:
                if i > j:
                    t += 1
            ans.append(t)
        return ans