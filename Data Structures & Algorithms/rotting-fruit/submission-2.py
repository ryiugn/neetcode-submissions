class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
        time = 0
        def addRotten(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append((r, c))
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addRotten(r + 1, c)
                addRotten(r - 1, c)
                addRotten(r, c + 1)
                addRotten(r, c - 1)
            time += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return time - 1 if time > 0 else time