class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = 1 if s[0] == 'R' else -1
        ans = 0
        for i in s[1:]:
            if i == 'R':
                c += 1
            else:
                c -= 1
            if c == 0:
                ans += 1
        return ans