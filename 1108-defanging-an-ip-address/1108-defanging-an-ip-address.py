class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ''
        for i in address:
            if i == '.':
                ans += f'[.]'
            else:
                ans += i
        return ans