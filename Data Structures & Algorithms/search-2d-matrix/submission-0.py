class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lastInd = len(matrix) * len(matrix[0]) - 1
        return self.binarySearch(matrix, 0, lastInd, target)

    def binarySearch(self, matrix, start, end, target):
        if start > end:
            return False
        mid = (start + end) // 2
        row = mid // len(matrix[0])
        col = mid % len(matrix[0])
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            return self.binarySearch(matrix, mid + 1, end, target)
        else:
            return self.binarySearch(matrix, start, mid-1, target)

        