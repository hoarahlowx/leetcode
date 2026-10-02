class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            temp = 0
            while n > 0:
                temp += n % 10
                n //= 10
            if i == temp:
                return i
        return -1