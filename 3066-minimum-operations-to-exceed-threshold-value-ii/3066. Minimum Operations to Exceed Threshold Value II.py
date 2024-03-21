class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heapq.heappush(q, num)
        count = 0
        while len(q) >= 2:
            if q[0] >=k: return count
            a = heapq.heappop(q)
            b = heapq.heappop(q)

            newElem = 2*a+b
            heapq.heappush(q, newElem)
            count+=1
        return count
            