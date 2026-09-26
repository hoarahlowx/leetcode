class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        ln = list(str(n))
        c = 0
        for i in range(len(ln)):
            c += int(ln[i])
        return c