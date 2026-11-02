class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for c in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1

            if matrix[c][l] > target or matrix[c][r] < target:
                continue

            while l <= r:
                middle = (l + r) // 2

                if matrix[c][middle] == target:
                    return True
                elif matrix[c][middle] > target:
                    r = middle - 1
                else:
                    l = middle + 1

        
        return False
