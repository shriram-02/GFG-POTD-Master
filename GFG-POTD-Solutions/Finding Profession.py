class Solution:
    def profession(self, level, pos):
        flips = bin(pos - 1).count('1')
        return "Doctor" if flips % 2 else "Engineer"