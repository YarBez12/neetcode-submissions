class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        reachPacific = [[0] * m for i in range(n)]
        reachAtlantic = [[0] * m for i in range(n)]
        qPacific = deque()
        qAtlantic = deque()
        for i in range(m):
            reachPacific[0][i] = 1
            reachAtlantic[-1][i] = 1
            qPacific.append((0, i))
            qAtlantic.append((n-1, i))
        for j in range(n):
            reachPacific[j][0] = 1
            reachAtlantic[j][-1] = 1
            qPacific.append((j, 0))
            qAtlantic.append((j,m-1))
        self.bfs(qPacific, reachPacific, heights)
        self.bfs(qAtlantic, reachAtlantic, heights)
        ans = []
        for i in range(n):
            for j in range(m):
                if reachAtlantic[i][j] and reachPacific[i][j]:
                    ans.append([i,j])
        return ans
    
    def bfs(self, q, reach, heights):
        n = len(heights)
        m = len(heights[0])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        while q:
            i, j = q.popleft()
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < m and not reach[x][y] and heights[x][y] >= heights[i][j]:
                    reach[x][y] = 1
                    q.append((x, y))

        