class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for i in range(len(board)):
        #     s = set()
        #     for num in board[i]:
        #         if num == ".":
        #             continue
        #         if num in s:
        #             return False
        #         s.add(num)
        
        # for i in range(len(board[0])):
        #     s = set()
        #     for j in range(len(board)):
        #         if board[j][i] == ".":
        #             continue
        #         if board[j][i] in s:
        #             return False
        #         s.add(board[j][i])

        # for ind1 in range(3):
        #     for ind2 in range(3):
        #         s = set()
        #         for i in range(ind1 * 3, (ind1 + 1) * 3):
        #             for j in range(ind2 * 3, (ind2 + 1) * 3):
        #                 if board[i][j] == ".":
        #                     continue
        #                 if board[i][j] in s:
        #                     return False
        #                 s.add(board[i][j])
        
        # return True

        N = 9

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(N):
            for j in range(N):
                val = board[i][j]
                if val == ".":
                    continue
                boxInd = (i // 3, j // 3)

                if val in rows[i] or val in cols[j] or val in boxes[boxInd]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[boxInd].add(val)
        return True