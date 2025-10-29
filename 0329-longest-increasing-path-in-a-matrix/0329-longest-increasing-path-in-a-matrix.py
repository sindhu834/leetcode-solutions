class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]  # memoization cache
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            
            max_len = 1  # minimum path length is 1 (itself)
            
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    length = 1 + dfs(x, y)
                    max_len = max(max_len, length)
            
            dp[i][j] = max_len
            return dp[i][j]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        
        return ans
