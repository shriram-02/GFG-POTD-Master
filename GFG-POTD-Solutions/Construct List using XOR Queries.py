class Solution:
    def constructList(self, queries):
        xr = 0
        arr = [0]

        for t, x in queries:
            if t == 0:
                arr.append(x ^ xr)
            else:
                xr ^= x

        return sorted(num ^ xr for num in arr)