class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        while r != l:
            border1, border2 = height[l], height[r]
            ans = max(ans, min(border1, border2) * (r - l))
            if border1 > border2:
                r -= 1
            else:
                l += 1
        return ans