class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        open = 0
        close = 0
        ans = []
        for i in seq:
            if i == '(':
                ans.append(open)
                close = open
                open = (open + 1) % 2
            if i == ')':
                ans.append(close)
                open = close
                close = (close + 1) % 2
        return ans