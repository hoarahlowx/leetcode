from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        dcv = deque()
        dcv.append(root)
        ans = 0
        while dcv:
            cur = len(dcv)
            for i in range(cur):
                t = dcv.popleft()
                if t.left:
                    dcv.append(t.left)
                if t.right:
                    dcv.append(t.right)

                if low <= t.val <= high:
                    ans += t.val
        return ans
