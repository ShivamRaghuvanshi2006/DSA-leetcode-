class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Create DP table (100 rows max as per constraints)
        dp = [[0.0] * (i + 1) for i in range(101)]
        
        dp[0][0] = poured
        
        for i in range(query_row + 1):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    excess = (dp[i][j] - 1) / 2.0
                    dp[i][j] = 1
                    dp[i + 1][j] += excess
                    dp[i + 1][j + 1] += excess
        
        return min(1, dp[query_row][query_glass])
