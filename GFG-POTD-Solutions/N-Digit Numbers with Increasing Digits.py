class Solution:
    def increasingNumbers(self, n):
        if n == 1:
            return [i for i in range(10)]
        if n > 9:
            return []

        ans = []

        def backtrack(start, path):
            if len(path) == n:
                ans.append(int("".join(map(str, path))))
                return
            for d in range(start, 10):
                path.append(d)
                backtrack(d + 1, path)
                path.pop()

        backtrack(1, [])
        return ans