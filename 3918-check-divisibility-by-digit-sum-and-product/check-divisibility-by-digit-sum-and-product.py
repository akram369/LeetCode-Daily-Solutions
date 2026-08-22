class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s, p = 0, 1
        for c in str(n):
            d = int(c)
            s += d
            p *= d
        return n % (s + p) == 0