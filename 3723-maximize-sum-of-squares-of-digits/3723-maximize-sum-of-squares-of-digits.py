class Solution:
    def maxSumOfSquares(self, num: int, sum_val: int) -> str:
        if sum_val > 9 * num or sum_val < 1:
            return ""
        
        nines = sum_val // 9
        rem = sum_val % 9
        
        if nines == num:
            return "9" * num
        
        zeros = num - nines - 1
        return "9" * nines + str(rem) + "0" * zeros