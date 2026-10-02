class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def gen(st='', op=0, cl=0):
            if op == cl == n:
                ans.append(st)
                return
            if op > cl:
                gen(st + ')', op, cl+1)
            if op < n:
                gen(st + '(', op+1, cl)
        gen()
        return ans
        