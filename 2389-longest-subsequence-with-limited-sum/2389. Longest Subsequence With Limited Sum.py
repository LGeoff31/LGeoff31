class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []

        prefix = []
        acc = 0
        for num in nums:
            acc+=num
            prefix.append(acc)
        print(prefix)
        for num in queries:
            if prefix[0] > num:
                res.append(0)
            else:
                valid = False
                for j in range(len(prefix)):
                    if prefix[j] > num:
                        res.append(j)
                        valid=True
                        break
                if not valid: res.append(len(nums))
        return res

        