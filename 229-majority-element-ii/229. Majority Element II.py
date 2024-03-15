class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int) #dict whre every number set to 0

        for num in nums:
            count[num] += 1

            if len(count) <= 2: #valid
                continue
            else:
                newCounter = defaultdict(int)
                for key in count:
                    if count[key] > 1:
                        newCounter[key] = count[key] - 1
                    # count[key] -= 1
                    # if count[key]!=0:
                    #     newCounter[key] = count[key]
                count = newCounter 
        n = len(nums) // 3
        res = []

        for key in count:
            if nums.count(key) > n:
                res.append(key)
        

        return res

