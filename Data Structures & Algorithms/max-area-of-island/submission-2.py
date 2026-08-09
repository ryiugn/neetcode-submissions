class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 0
            if grid[i][j] == 1:
                grid[i][j] = 0
                return (1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))
        return res