class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d1, d2 = {}, {}
        ans = 0
        for i in range(len(s)):
            d1[s[i]] = i
            d2[t[i]] = i
        for i in d1.items():
            ans += abs(i[1] - d2[i[0]])
        return ans