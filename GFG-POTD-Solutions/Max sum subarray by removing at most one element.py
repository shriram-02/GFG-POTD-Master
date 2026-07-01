class Solution:
    def maxSumSubarray(self, arr):
        no_del = arr[0]
        one_del = float("-inf")
        ans = arr[0]

        for i in range(1, len(arr)):
            one_del = max(no_del, one_del + arr[i])
            no_del = max(arr[i], no_del + arr[i])
            ans = max(ans, no_del, one_del)

        return ans