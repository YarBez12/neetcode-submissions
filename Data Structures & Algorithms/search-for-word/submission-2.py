class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.check(board, word, i, j, {(i, j)}, board[i][j]):
                    return True
        return False


    def check(self, board, word, row, col, used, curr):
        if curr == word:
            return True
        if len(curr) > len(word):
            return False
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        for d in dirs:
            x = row + d[0]
            y = col + d[1]
            if (x, y) in used or x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                continue
            curr += board[x][y]
            used.add((x, y))
            if self.check(board, word, x, y, used, curr):
                return True
            curr = curr[:-1]
            used.remove((x,y))

        
        return False
        