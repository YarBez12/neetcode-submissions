class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # i, j: column = n - i; row = j
        n = len(matrix)
        for i in range((n+1)//2):
            for j in range(i,n-i-1):
                x, y = i, j
                curr = matrix[i][j]
                for k in range(4):
                    t = matrix[y][n-x-1]
                    matrix[y][n-x-1] = curr
                    curr = t
                    x, y = y, n-x-1
        