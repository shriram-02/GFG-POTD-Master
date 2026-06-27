class Solution:
    def countWays(self, n, m):
        MOD = 10**9 + 7

        if n < m:
            return 1

        dp = [0] * (n + 1)

        for i in range(n + 1):
            if i < m:
                dp[i] = 1
            elif i == m:
                dp[i] = 2
            else:
                dp[i] = (dp[i - 1] + dp[i - m]) % MOD

        return dp[n]