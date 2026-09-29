class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                grid[i][j] = "0"
                q = deque()
                q.append((i,j))
                while q:
                    x, y = q.popleft()
                    for d in dirs:
                        nx = x + d[0]
                        ny = y + d[1]
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                            grid[nx][ny] = "0"
                            q.append((nx, ny))
                islands += 1
        return islands