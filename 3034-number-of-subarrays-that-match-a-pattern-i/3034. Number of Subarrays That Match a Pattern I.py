class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        res = 0
        for i in range(len(nums) - len(pattern)):
            subarr = nums[i:i+len(pattern)+1]
            valid = True
            for j in range(len(subarr)-1):
                if subarr[j+1] > subarr[j] and pattern[j]!=1: valid=False
                if subarr[j+1] < subarr[j] and pattern[j]!=-1: valid=False
                if subarr[j+1] == subarr[j] and pattern[j]!=0: valid=False
            if valid: res+=1
        return res
        