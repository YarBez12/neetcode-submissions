class Solution:
    # 1st approach
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     maxArea = 0
    #     dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j] == 0:
    #                 continue
    #             grid[i][j] = 0
    #             q = deque()
    #             q.append((i,j))
    #             currArea = 1
    #             while q:
    #                 x, y = q.popleft()
    #                 for d in dirs:
    #                     nx = x + d[0]
    #                     ny = y + d[1]
    #                     if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
    #                         grid[nx][ny] = 0
    #                         q.append((nx, ny))
    #                         currArea += 1
    #             maxArea = max(currArea, maxArea)
    #     return maxArea

    # 2nd approach
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                currArea = self.dfs(grid, i, j)
                maxArea = max(currArea, maxArea)
        return maxArea
    
    def dfs(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])
        if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        area = 1
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        for dx, dy in dirs:
            area += self.dfs(grid, i+dx, j+dy)
        return area