class Solution:
    def maxArea(self, height):
        n = len(height)
        if n < 2:
            return 0

        i, j = 0, n - 1
        ans = 0

        while i < j:
            ans = max(ans, min(height[i], height[j]) * (j - i - 1))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return ans