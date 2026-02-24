class Solution:
    def minScoreTriangulation(self, values):
        n = len(values)
        
        # Create DP table
        dp = [[0] * n for _ in range(n)]
        
        # length is gap between i and j
        for length in range(2, n):  
            for i in range(n - length):
                j = i + length
                dp[i][j] = float('inf')
                
                for k in range(i + 1, j):
                    cost = (dp[i][k] +
                            dp[k][j] +
                            values[i] * values[k] * values[j])
                    
                    dp[i][j] = min(dp[i][j], cost)
        
        return dp[0][n-1]