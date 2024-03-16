class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        a = set(arr)
        for i in range(1, arr[-1]):
            if i not in a: missing.append(i)
        if k-1 >= len(missing):
            diff = k-1 - len(missing)
            return arr[-1] + diff + 1
        return missing[k-1]



        