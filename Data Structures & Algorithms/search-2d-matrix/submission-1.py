class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for i in range(len(matrix)):
            left = 0
            right = len(matrix[i]) - 1

            if matrix[i][left] <= target and matrix[i][right] >= target:
                while left <= right:
                    middle = (left + right) // 2
                    if matrix[i][middle] < target:
                        left = middle + 1
                    elif matrix[i][middle] > target:
                        right = middle - 1
                    else:
                        return True
            else:
                continue
        
        return False