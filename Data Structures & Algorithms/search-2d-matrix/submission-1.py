class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        while up <= down:
            m = (down + up) // 2
            if target > matrix[m][-1]:
                up = m + 1
            elif target < matrix[m][0]:
                down = m - 1
            else:
                l, r = 0, len(matrix[0]) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[m][mid] < target:
                        l = mid + 1
                    elif matrix[m][mid] > target:
                        r = mid - 1
                    else:
                        return True
                return False
        return False