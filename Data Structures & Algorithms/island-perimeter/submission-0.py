class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in dirs:
                        x, y = i+dx, j+dy
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                            ans += 1
        return ans
        