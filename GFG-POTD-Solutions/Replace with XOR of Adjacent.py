class Solution:
    def replaceElements(self, arr):
        n = len(arr)
        temp = arr[:]  # copy of original array

        arr[0] = temp[0] ^ temp[1]

        for i in range(1, n - 1):
            arr[i] = temp[i - 1] ^ temp[i + 1]

        arr[n - 1] = temp[n - 2] ^ temp[n - 1]

        return arr