class Solution:
    def getLastDigit(self, a, b):
        if b == "0":
            return 1

        last = int(a[-1])
        exp = int(b[-2:]) if len(b) >= 2 else int(b)

        cycle = [last]
        x = last
        while True:
            x = (x * last) % 10
            if x == cycle[0]:
                break
            cycle.append(x)

        return cycle[(exp - 1) % len(cycle)]