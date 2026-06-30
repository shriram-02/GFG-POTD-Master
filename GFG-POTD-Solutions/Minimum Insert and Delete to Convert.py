class Solution:
    def minInsAndDel(self, a, b):
        pos = {x: i for i, x in enumerate(b)}
        arr = [pos[x] for x in a if x in pos]

        lis = []
        from bisect import bisect_left

        for x in arr:
            i = bisect_left(lis, x)
            if i == len(lis):
                lis.append(x)
            else:
                lis[i] = x

        lcs = len(lis)
        return (len(a) - lcs) + (len(b) - lcs)