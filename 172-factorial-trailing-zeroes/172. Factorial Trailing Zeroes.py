class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        res = 0
        exponent = 1
        while (5**exponent) <= n:
            res += n // (5**exponent)
            exponent += 1
        return res
        