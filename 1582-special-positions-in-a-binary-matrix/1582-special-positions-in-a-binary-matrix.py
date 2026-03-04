class Solution:
    def numSpecial(self, mat):
        m, n = len(mat), len(mat[0])
        
        rowCount = [0] * m
        colCount = [0] * n
        
        # Count 1s in rows and columns
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1
        
        # Count special positions
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rowCount[i] == 1 and colCount[j] == 1:
                    count += 1
        
        return count