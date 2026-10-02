class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        for i in range(m):
            self.dfs(board, 0, i)
            self.dfs(board, n-1, i)
        for i in range(n):
            self.dfs(board, i, 0)
            self.dfs(board, i, m-1)
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "W":
                    board[i][j] = "O" 
    
    def dfs(self, board, row, col):
        n = len(board)
        m = len(board[0])
        if row < 0 or col < 0 or row >= n or col >= m or board[row][col] != "O":
            return
        board[row][col] = "W"
        dirs = [(0,1), (1,0), (0,-1),(-1,0)]
        for dx, dy in dirs:
            x = row + dx
            y = col + dy
            self.dfs(board, x, y)
        