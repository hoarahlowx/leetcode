from functools import lru_cache


class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        ans = False
        n, m = len(grid) - 1, len(grid[0]) - 1

        if grid[0][0] == ')' or grid[n][m] == '(':
            return False
        
        @lru_cache(None)
        def dfs(cur, i, j):
            cur += 1 if grid[i][j] == '(' else -1
            
            if cur < 0:
                return False
            
            if cur > (n - i) + (m - j):
                return False

            if i == n and j == m:
                return cur == 0
            
            if i < n and dfs(cur, i + 1, j):
                return True
            if j < m and dfs(cur, i, j + 1):
                return True

            return False


        return dfs(0, 0, 0)