class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshCount = 0
        n = len(grid)
        m = len(grid[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    freshCount += 1
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        minutes = 0
        while q:
            minutes += 1
            num = len(q)
            for k in range(num):
                i, j = q.popleft()
                for dx, dy in dirs:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x,y))
                        freshCount -= 1
        return max(minutes-1,0) if freshCount == 0 else -1

        