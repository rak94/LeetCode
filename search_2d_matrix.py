from typing import List

class Search2DMatrix:
    def matrix_search(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        topRow, bottomRow = 0, ROWS - 1

        while topRow <= bottomRow:
            midRow = (topRow + bottomRow) // 2
            if target > matrix[midRow][-1]:
                topRow = midRow + 1
            elif target < matrix[midRow][0]:
                bottomRow = midRow - 1
            else:
                break
        
        if not (topRow <= bottomRow):
            return False
        midRow = (topRow + bottomRow) // 2
        left, right = 0, COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[midRow][mid]:
                left = mid + 1
            elif target < matrix[midRow][mid]:
                right = mid - 1
            else:
                return True
        return False
