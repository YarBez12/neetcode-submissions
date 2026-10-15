class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs1 = [(0,1), (1,0)]
        dirs2 = [(0,-1), (-1,0)]
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        rows = [0, m-1]
        cols = [0, n-1]
        while rows[0] <= rows[1] and cols[0] <= cols[1]:
            x, y = rows[0], cols[0]
            ans.append(matrix[x][y])

            for dx, dy in dirs1:
                while rows[0] <= x + dx <= rows[1] and cols[0] <= y + dy <= cols[1]:
                    x += dx
                    y += dy
                    ans.append(matrix[x][y])
            
            rows[0] += 1
            cols[1] -= 1

            for dx, dy in dirs2:
                while rows[0] <= x + dx <= rows[1] and cols[0] <= y + dy <= cols[1]:
                    x += dx
                    y += dy
                    ans.append(matrix[x][y])
            rows[1] -= 1
            cols[0] += 1
        return ans

            
        