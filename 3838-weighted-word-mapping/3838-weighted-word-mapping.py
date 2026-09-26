class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ''
        for i in words:
            temp = 0
            for j in i:
                  temp += weights[ord(j) - 97]
            temp %= 26
            ans += chr(97 + (25 - temp))
        return ans

s = Solution()
print(s.mapWordWeights(["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))