class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        
        firstRowZero = False
        firstColZero = False

        # Check first column
        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True
                break

        # Check first row
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = True
                break

        # Mark rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set rows to zero
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        # Set columns to zero
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        # Set first row and column if needed
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0

        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0
