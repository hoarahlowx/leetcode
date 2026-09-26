from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        def backtrack(cur: str, ln_cur: int) -> None:
            if ln_cur == n:
                ans.append(cur)
                return
            cur += '1'
            backtrack(cur, ln_cur + 1)
            cur = cur[:-1]

            if not cur or cur[-1] != "0":
                cur += '0'
                backtrack(cur, ln_cur + 1)
                cur = cur[:-1]
        backtrack('', 0)
        return ans
    