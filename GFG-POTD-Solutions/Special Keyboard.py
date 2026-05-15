class Solution:

    def optimalKeys(self, n: int) -> int:
        if n <= 6:
            return n
        
        dp = [0] * (n + 1)
        
        for i in range(1, 7):
            dp[i] = i
        
        for i in range(7, n + 1):
            dp[i] = 0
            
            for j in range(i - 3, 0, -1):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        
        return dp[n]