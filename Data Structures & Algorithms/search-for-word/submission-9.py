class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.check(board, word, i, j, 1):
                    return True
        return False


    def check(self, board, word, row, col, curr):
        if curr >= len(word):
            return True
        prev = board[row][col]
        board[row][col] = "#"
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        for d in dirs:
            x = row + d[0]
            y = col + d[1]
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != word[curr]:
                continue
            if self.check(board, word, x, y, curr+1):
                board[row][col] = prev
                return True
        board[row][col] = prev

        
        return False
        