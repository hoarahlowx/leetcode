class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans = ''
        for i in s:
            if k == 0:
                break
            if i == ' ':
                k -= 1
            ans += i
        return ans.rstrip()