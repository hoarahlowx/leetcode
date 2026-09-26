from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i in range(len(boxes)):
            t = 0
            l, r = i - 1, i + 1
            while l > -1:
                t += int(boxes[l]) * abs(i - l)
                l -= 1
            while r < len(boxes):
                t += int(boxes[r]) * abs(i - r)
                r += 1
            ans.append(t)
        return ans