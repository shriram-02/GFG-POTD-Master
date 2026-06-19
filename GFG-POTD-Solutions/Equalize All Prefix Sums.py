class Solution:
    def optimalArray(self, arr):
        n = len(arr)
        pre = [0] * (n + 1)

        for i in range(n):
            pre[i + 1] = pre[i] + arr[i]

        ans = [0] * n

        for i in range(n):
            m = i // 2
            med = arr[m]

            left = med * (m + 1) - pre[m + 1]
            right = (pre[i + 1] - pre[m + 1]) - med * (i - m)

            ans[i] = left + right

        return ans