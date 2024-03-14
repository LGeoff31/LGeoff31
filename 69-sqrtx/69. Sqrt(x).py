from math import floor
#Time Complexity: O(sqrt(x))
#Space Complexity: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        i = 1
        while True:
            if i * i <= x and (i+1) * (i+1) > x:
                return i
            i += 1
