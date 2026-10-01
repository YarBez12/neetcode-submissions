class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        ans = []
        self.backtrack(board, 0, ans)
        return ans

    
    def backtrack(self, board, col, ans):
        if col == len(board):
            ans.append(["".join(row) for row in board])
            return 
        for i in range(len(board)):
            if self.isValid(board, i, col):
                board[i][col] = "Q"
                self.backtrack(board, col+1, ans)
                board[i][col] = "."
    
    def isValid(self, board, row, col):
        for i in range(col):
            if board[row][i] == "Q":
                return False
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        i, j = row, col
        while i < len(board) and j >= 0:
            if board[i][j] == "Q":
                return False
            i += 1
            j -= 1
        return True
        