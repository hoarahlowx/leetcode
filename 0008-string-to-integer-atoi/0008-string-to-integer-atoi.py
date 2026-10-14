class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == '':
            return 0

        ans = 0
        dig = '0123456789'
        neg = 1
        
        if s[0] == '-':
            neg = -1
        elif s[0] == '+':
            neg = 1
        elif s[0] in dig:
            ans = int(s[0])
        else:
            return 0
        
        for i in s[1:]:
            if i in dig:
                is_dig = True
                ans *= 10
                ans += int(i)
                if neg * ans >= 2147483648:
                    return 2147483647
                elif neg * ans <= -2147483648:
                    return -2147483648
            else:
                return neg * ans
        return neg * ans
            