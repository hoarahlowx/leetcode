class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        ans = []
        for i in order:
            if i in friends:
                ans.append(i)
        return ans