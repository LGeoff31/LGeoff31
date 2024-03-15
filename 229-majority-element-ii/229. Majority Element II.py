class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)

        a = len(nums)//3
        res = []
        for key in dic:
            if dic[key] > a:
                res.append(key)
        return res
                
        