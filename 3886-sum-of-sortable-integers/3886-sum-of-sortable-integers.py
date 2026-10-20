from math import sqrt
from array import array


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        divisors = []
        n = len(nums)
        sorted_nums = sorted(nums)
        ans = 0

        for i in range(1, int(sqrt((len(nums)+1)) + 1)):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)

        if nums == sorted_nums:
            return sum(divisors)

        nums = array('i', nums)
        mv = memoryview(nums)

        for i in divisors[1:]:
            picks = [-99999]
            total_agree = True
            for j in range(i, len(nums) + 1, i):
                screen = mv[j-i:j]
                pick = None
                foot = None
                agree = True
                for el in range(1, len(screen)):
                    if screen[el-1] > screen[el] and pick is None:
                        pick = screen[el-1]
                        foot = screen[el]
                    elif screen[el-1] > screen[el]:
                        agree = False
                        break

                if agree and pick is None:
                    pick = screen[-1]
                    foot = screen[0]
                else:
                    if screen[0] < screen[-1]:
                        total_agree = False
                        break
                if agree and picks[-1] <= foot:
                    picks.append(pick)
            
                else:
                    total_agree = False
                    break
            if total_agree:
                ans += i
        return ans
