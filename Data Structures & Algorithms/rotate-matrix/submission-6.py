class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # i, j: column = n - i; row = j
        # 1st approach
        # n = len(matrix)
        # for i in range((n+1)//2):
        #     for j in range(i,n-i-1):
        #         x, y = i, j
        #         curr = matrix[i][j]
        #         for k in range(4):
        #             t = matrix[y][n-x-1]
        #             matrix[y][n-x-1] = curr
        #             curr = t
        #             x, y = y, n-x-1

        # 2nd approach
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for r in matrix:
            r.reverse()
        