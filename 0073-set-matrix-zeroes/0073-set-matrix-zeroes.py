from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        # Variables to mark if the first row and first column should be zeroed
        first_row_has_zero = False
        first_col_has_zero = False
        
        # Determine if first row or first column should be zeroed
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
                
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        # Use first row and first column to mark rows and columns that need to be zeroed
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Zero out cells based on the marks in the first row and first column
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        # Zero out the first row if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero out the first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
