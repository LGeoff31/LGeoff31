class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        l, r = 0, 1

        while r < len(nums):
            if nums[r] <= nums[l]:
                l=r
                r+=1
            elif nums[r] - nums[l] > 0:
                res = max(res, nums[r] - nums[l])
                r += 1
        return res
        