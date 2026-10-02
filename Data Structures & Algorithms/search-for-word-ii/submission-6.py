class TrieNode:
    def __init__(self, word=False, children=None):
        self.word = word
        self.children = children if children is not None else {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = PrefixTree()
        for word in words:
            tree.insert(word)
        ans = []
        root = tree.root
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    self.check(board, i, j, 1, root.children[board[i][j]], ans)
        return ans
    
    def check(self, board, row, col, curr, node, ans):
        if node.word:
            ans.append(node.word)
            node.word = None
        n = len(board)
        m = len(board[0])
        prev = board[row][col]
        board[row][col] = "#"
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        for d in dirs:
            x = row + d[0]
            y = col + d[1]
            if x < 0 or y < 0 or x >= n or y >= m or board[x][y] not in node.children:
                continue
            self.check(board, x, y, curr+1, node.children[board[x][y]], ans)
        board[row][col] = prev        


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.word = word