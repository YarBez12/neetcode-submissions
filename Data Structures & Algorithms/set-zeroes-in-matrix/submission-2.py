class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        firstRow = False
        firstCol = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    if not firstRow and i == 0:
                        firstRow = True
                    if not firstCol and j == 0:
                        firstCol = True
        
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(n):
            if matrix[0][j] == 0 and (j != 0 or firstCol):
                for i in range(m):
                    matrix[i][j] = 0
        if firstRow:
            for j in range(n):
                    matrix[0][j] = 0

        
        