class Solution:
    def checkElements(self, start, end, arr):
        s = set(arr)
        
        for x in range(start, end + 1):
            if x not in s:
                return False
        
        return True