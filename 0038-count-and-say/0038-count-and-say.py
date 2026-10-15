class Solution:
    def countAndSay(self, n: int) -> str:
        def recursion(r):
            if r == 1:
                return "1"
            back = recursion(r - 1)
            et = back[0]
            count = 1
            ans = ''
            for i in back[1:]:
                if i != et:
                    ans += str(count) + et
                    count = 1
                else:
                    count += 1
                et = i
            ans += str(count) + et
            return ans
        return recursion(n)