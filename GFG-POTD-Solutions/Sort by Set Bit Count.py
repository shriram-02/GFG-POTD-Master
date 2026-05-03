class Solution:
    def sortBySetBitCount(self, arr):
        arr.sort(key=lambda x: bin(x).count('1'), reverse=True)
        return arr