class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        temp = ''
        for i in s:
            if i.lower() in valid:
                temp += i.lower()
        for i in range(len(temp)):
            if temp[i] != temp[len(temp) - 1 - i]:
                return False
        return True