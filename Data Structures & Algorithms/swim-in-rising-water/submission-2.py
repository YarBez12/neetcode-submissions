class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        times = {(i,j): float("inf") for i in range(n) for j in range(m)}
        h = [(grid[0][0], (0,0))]
        times[(0,0)] = grid[0][0]
        while h:
            currTime, cell = heapq.heappop(h)
            if currTime > times[cell]:
                continue
            i, j = cell
            dirs = [(0,1), (1,0), (0,-1), (-1,0)]
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < m:
                    time = max(currTime, grid[x][y])
                    if time < times[(x,y)]:
                        times[(x, y)] = time
                        heapq.heappush(h, (time, (x,y)))
        return times[(n-1, m-1)]
        