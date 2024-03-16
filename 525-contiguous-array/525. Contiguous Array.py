class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeroCount, oneCount = 0, 0
        dic = {}

        acc = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1: oneCount += 1
            else: zeroCount += 1

            if oneCount - zeroCount not in dic:
                dic[oneCount - zeroCount] = i
            
            if zeroCount == oneCount:
                res = max(res, 2*oneCount)
            elif oneCount - zeroCount in dic:
                res = max(res,i - dic[oneCount - zeroCount])
        return res