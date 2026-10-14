class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        ans = 0
        while r < len(s):
            if s[r] in s[l:r]:
                ans = max(ans, (r - l))
                while s[l] != s[r]:
                    l += 1
                l += 1
            r += 1
        ans = max(ans, (r - l))
        return ans