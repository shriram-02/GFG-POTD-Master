class Solution:
    def maxDotProduct(self, a, b):
        n, m = len(a), len(b)

        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i - 1][j - 1] + a[i - 1] * b[j - 1]
                )

        return dp[n][m]