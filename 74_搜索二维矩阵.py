class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        low,high = 0,len(matrix)-1
        key = None
        while low <= high:
            mid = low + (high - low) // 2
            if target > matrix[mid][-1]:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                key = mid
                break
        if key is None: return False
        else:
            low,high = 0,len(matrix[key]) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if matrix[key][mid] < target:
                    low = mid + 1
                elif matrix[key][mid] > target:
                    high = mid - 1
                else:
                    return True
            return False