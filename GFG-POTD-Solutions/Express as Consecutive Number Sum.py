class Solution:
    def isSumOfConsecutive(self, n: int) -> bool:
        # code here
        return (n & (n - 1)) != 0