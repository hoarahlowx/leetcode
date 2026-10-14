class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            cur = (l + r) // 2
            if nums[cur] == target:
                return cur
            if nums[cur] < target:
                l = cur + 1
            else:
                r = cur - 1
        return l