class Solution:
    def numberOfCuts(self, n: int) -> int:
        #1 -> 2
        #2 -> 4 or 3
        #3 -> 6
        #4 -> 8
        if n == 1: return 0
        if n % 2 == 0:
            return n//2
        else:
            return n
        # return n//2 + n%2
        