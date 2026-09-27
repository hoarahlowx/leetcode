from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_list(root: Optional[TreeNode]) -> List:
    result = []
    q = deque([root])
    while q:
        level_size = len(q)
        for _ in range(level_size):
            node = q.popleft()
            result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return sorted(result)



class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        st = tree_to_list(root)
        queue = deque([root])

        while queue:
            node = queue.popleft()

            node.val = node.val + sum([i for i in st if i > node.val])
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root