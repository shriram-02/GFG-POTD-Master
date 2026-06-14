class Solution:
    def minimumCost(self, cost, w):
        INF = float('inf')

        dp = [INF] * (w + 1)
        dp[0] = 0

        n = len(cost)

        for i in range(1, w + 1):
            for j in range(n):
                wt = j + 1

                if cost[j] != -1 and wt <= i:
                    dp[i] = min(dp[i], dp[i - wt] + cost[j])

        return -1 if dp[w] == INF else dp[w]