class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        seen = set()
        q = deque()
        inf = 2 ** 31 - 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        rounds = 1
        while q:
            num = len(q)
            for k in range(num):
                i, j = q.popleft()
                for dx, dy in dirs:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == inf:
                        grid[x][y] = rounds
                        q.append((x,y))
            rounds += 1
