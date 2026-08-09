class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        temp = [0]
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited:
                return
            if grid[i][j] == 0:
                return
            if grid[i][j] == 1:
                temp[0] += 1
                visited.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    temp[0] = 0
                    dfs(r, c)
                    res = max(res, temp[0])
        return res