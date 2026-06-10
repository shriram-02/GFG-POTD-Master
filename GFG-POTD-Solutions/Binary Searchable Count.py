class Solution:
    def binarySearchable(self, arr):
        self.ans = 0

        def dfs(l, r, low, high):
            if l > r:
                return

            mid = (l + r) // 2
            val = arr[mid]

            if low < val < high:
                self.ans += 1

            dfs(l, mid - 1, low, min(high, val))
            dfs(mid + 1, r, max(low, val), high)

        dfs(0, len(arr) - 1, float('-inf'), float('inf'))
        return self.ans