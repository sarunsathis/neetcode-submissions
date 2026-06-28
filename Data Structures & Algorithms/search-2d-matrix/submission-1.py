class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        low = mid = 0
        high = r

        for arr in matrix :
            if arr[-1] == target :
                return True
            elif arr[-1] > target :
                low = mid = 0
                high = len(arr)
                while low <= high :
                    mid = (low + high) // 2
                    if arr[mid] == target :
                        return True
                    elif arr[mid] > target :
                        high = mid - 1
                    else :
                        low = mid + 1
                return False
        
        return False