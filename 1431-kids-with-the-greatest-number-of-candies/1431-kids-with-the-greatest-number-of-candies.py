class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        for i in candies:
            f = True
            for j in candies:
                if i + extraCandies < j:
                    f = False
                    break
            ans.append(f)
        return ans