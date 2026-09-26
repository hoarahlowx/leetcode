class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        ans = [first]
        c = 0
        for i in encoded:
            ans.append(i ^ ans[c])
            c += 1
        return ans