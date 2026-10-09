class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target: 
                l = m + 1
            else:
                break
        # midpoint is the array
        row = matrix[m]
        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if row[m] > target:
                r = m - 1
            if row[m] < target:
                l = m + 1
            if row[m] == target:
                return True
        return False


            
        