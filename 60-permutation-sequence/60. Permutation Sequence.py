class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return ''.join([str(i) for i in sorted(list(permutations([i for i in range(1, n+1)], n)))[k-1]])
        


        