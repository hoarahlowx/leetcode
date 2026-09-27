class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for i in words:
            f = True
            for j in i:
                if j not in allowed:
                    f = False
                    break
            if f:
                ans += 1
        return ans