from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        for i in range(len(A)):
            ans.append(len(set(A[0:i+1]) & set(B[0:i+1])))
        return ans