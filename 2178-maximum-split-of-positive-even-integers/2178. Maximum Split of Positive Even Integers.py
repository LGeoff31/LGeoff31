class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1: return [] 
        k = int((-1+math.sqrt(1+4*finalSum)) // 2)
        a = []
        b = 2
        currSum = 2
        for i in range(k-1):
            a.append(b)
            b+=2
            currSum+=b
        currSum-=b
        print(a)

        a.append(finalSum - currSum)

        return a

        