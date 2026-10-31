class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        col = 0

        for col in range(len(matrix)):
            left = 0
            right = len(matrix[col]) - 1
            if matrix[col][left] <= target and matrix[col][right] >= target:
                while left <= right:
                    middle = (left+right) // 2
                    if matrix[col][middle] == target:
                        return True
                    elif matrix[col][middle] > target:
                        right = right - 1
                    else:
                        left = left + 1


        return False
        