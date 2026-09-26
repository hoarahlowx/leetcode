import string


def in_base(n, base):
    alphabet = string.ascii_letters + string.digits
    ans = ''
    while n > 0:
        ans = alphabet[n%base] + ans
        n //= base
    return ans


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            temp = in_base(n, i)
            if temp != temp[::-1]:
                return False
        return True