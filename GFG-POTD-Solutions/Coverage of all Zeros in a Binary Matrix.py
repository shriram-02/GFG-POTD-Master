class Solution:
    def findCoverage(self, mat):
        n = len(mat)
        m = len(mat[0])
        ans = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    if any(mat[i][k] == 1 for k in range(j - 1, -1, -1)):
                        ans += 1
                    if any(mat[i][k] == 1 for k in range(j + 1, m)):
                        ans += 1
                    if any(mat[k][j] == 1 for k in range(i - 1, -1, -1)):
                        ans += 1
                    if any(mat[k][j] == 1 for k in range(i + 1, n)):
                        ans += 1

        return ans