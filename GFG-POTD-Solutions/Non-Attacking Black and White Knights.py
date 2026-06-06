class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        total = n * m
        attacking = 0

        if n > 1 and m > 2:
            attacking += (n - 1) * (m - 2)
        if n > 2 and m > 1:
            attacking += (n - 2) * (m - 1)

        attacking *= 4

        return total * (total - 1) - attacking