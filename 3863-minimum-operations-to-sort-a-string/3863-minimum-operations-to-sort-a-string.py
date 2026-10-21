class Solution:
    def minOperations(self, s: str) -> int:
        s = list(s)
        if len(s) == 2 and sorted(s) != s:
            return -1
        elif sorted(s) == s:
            return 0

        mn, mx = s[0], s[0]
        mni, mxi = 0, 0
        for i in range(1, len(s)):
            if s[i] < mn:
                mn = s[i]
                mni = i
            if s[i] >= mx:
                mx = s[i]
                mxi = i

        if mn == s[0] or mx == s[-1]:
            return 1
        if mni < len(s) - 1 or mxi > 0:
            return 2
        else:
            return 3